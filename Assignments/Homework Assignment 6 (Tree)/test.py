import sys
import textwrap
import ast



class TreeWithoutParent:
    def __init__(self, element, children=None):
        self._element = element
        self._children = children if children else []

    def __str__(self):
        return str(self._element)

    def pretty_print(self, indent=0):
        print('  ' * indent + str(self._element))
        for child in self._children:
            child.pretty_print(indent + 1)


def trees_equal(node1, node2):
    if node1._element != node2._element:
        return False

    if len(node1._children) != len(node2._children):
        return False

    for child1, child2 in zip(node1._children, node2._children):
        if not trees_equal(child1, child2):
            return False

    return True

def _resolve_level_of_lines(lines:list)->list:
    lv_list = []
    for line in lines:
        num_of_space = len(line) - len(line.strip())
        lv = num_of_space // 3
        if num_of_space!=lv*3:
            raise SyntaxError("can't resolve input: wrong indention")
        lv_list.append(lv)
    return lv_list

def extract_outermost_parentheses(text):
    stack = []
    start = -1
    for i, char in enumerate(text):
        if char == '(':
            if not stack:
                start = i
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
                if not stack and start != -1:
                    return text[start:i+1]
    return None

def _expr_to_tree(ast_list:list, lv_list:list, current_line, lv) -> (TreeWithoutParent, int):
    operator_mapping = {"And": "and","Or": "or","Add": "+","Sub": "-","Mult": "*","MatMult": "@",  "Div": "/","Mod": "%"
        ,"Pow": "**","LShift": "<<","RShift": ">>","BitOr": "|","BitXor": "^","BitAnd": "&","FloorDiv": "//"
        ,"Invert": "~","Not": "not","UAdd": "+","USub": "-","Eq": "==","NotEq": "!=","Lt": "<","LtE": "<=","Gt": ">",
        "GtE": ">=","Is": "is","IsNot": "is not","In": "in","NotIn": "not in"}

    op_kws_list = ['op', 'ops']
    expr_kws_list = ['values', 'target', 'value', 'left', 'right', 'operand', 'body', 'test', 'orelse', 'keys',
                     'elts', 'elt', 'key', 'comparators', 'func', 'args', 'format_spec', 'slice']# 如果匹配到value需要检测是否是constant
    idf_kws_list = ['attr', 'id']
    other_list = ['generators', 'keywords', 'cyx']# comprehension, argument, keywords, expr_context
    params = []
    root = None


    if lv_list[current_line+1]<=lv: # 单行表达式
        # print(f"current_line:{current_line}, lv:{lv}, 单行")
        # 单行表达式一般形式如下
        # e.g. func=Name(id='func_call', ctx=Load()),
        # 有限测试集中只会出现expr = Name, Constant, 进行对应处理即可
        #匹配最外层的括号：
        match = extract_outermost_parentheses(ast_list[current_line])

        # 匹配到内容如下：“id='func_call', ctx=Load()”  或  “value=0)]”  或  “id='a', ctx=Load())))]”
        # 需要处理冗余括号以及空格
        try:
            param_list = match.split(',')
        except AttributeError as e:
            print(f"line: {current_line}, line_str: {ast_list[current_line]}\n"
                  f"exception info: {e}")
            sys.exit(1)
        current_line += 1
        for param in param_list:
            if 'id' in param:
                return TreeWithoutParent(param.strip('[]() ').split('=')[1].strip("'\"")), current_line
            elif 'value' in param:
                return TreeWithoutParent(param.strip('[]() ').split('=')[1].strip("'\"")), current_line

        raise ValueError(f'met unsupported parameter for expr in line {current_line}\n'
                         f'line info: {ast_list[current_line]}')

    else:  #多行表达式
        current_line += 1
        while True:
            # 如果遇到低等级对象或者同级对象，说明本条已经结束返回node节点，与最新一行的idx
            if lv_list[current_line] < lv + 1 or current_line > len(lv_list) :
                if root:
                    root._children = params
                    return root, current_line
                elif len(params) == 1:
                    return params[0], current_line
                else:
                    raise ValueError(f"went wrong at line {current_line} when transforming. \n"
                                 f"line information {ast_list[current_line]}\n"
                                 f"Can't find a root node among {[node._element for node in params]}")

            # 如果遇到高于当前级别两级或以上的时候，表示indention出现错误，或是程序出现异常，抛出异常
            elif lv_list[current_line] > lv + 1:
                raise ValueError(f"went wrong at line {current_line} when transforming. \n"
                                 f"line information {ast_list[current_line]}\n")

            # 当遇到刚好高一级的对象时，表示此行为expr的参数。进行处理
            else:
                # print(f"current_line:{current_line}, lv:{lv}， root:{root}")
                expr_item = ast_list[current_line].split("=")[0].strip().split('(')[-1]

                # 当参数是expr时, 递归获取此expr转换为树后的根节点，将其放进params中
                if expr_item in expr_kws_list:
                    node, current_line = _expr_to_tree(ast_list, lv_list, current_line, lv+1)
                    params.append(node)

                # 当参数是operator时，它应当是root节点
                elif expr_item in op_kws_list:
                    if lv_list[current_line+1] <= lv_list[current_line]: # 单行
                        op_str = ast_list[current_line].split('=')[1].strip('[](), ')
                        root = TreeWithoutParent(operator_mapping[op_str])
                        current_line += 1
                    else: # 多行
                        current_line += 1
                        op_str = ast_list[current_line].strip('[](), ')
                        root = TreeWithoutParent(operator_mapping[op_str])
                        current_line += 1

                # 在有限测试集中，identifier对象只可能出现在单行表达式中，如遇到则抛出异常
                elif expr_item in idf_kws_list:
                    # raise ValueError(f'met unsupported expr_item {expr_item} in line {current_line}\n'
                    #       f'line info: {ast_list[current_line]}')
                    var = ast_list[current_line].split('\'')[1]
                    params.append(TreeWithoutParent(var))
                    current_line += 1

                else:
                    # 如果遇到不支持的expr，则代表不需要处理，直接跳过，直到同级对象出现
                    current_line += 1
                    print(f'met unsupported expr_item {expr_item} in line {current_line}\n'
                          f'line info: {ast_list[current_line]}')
                    while lv_list[current_line] > lv + 1:
                        current_line += 1
    # return TreeWithoutParent("An Expression"), current_line+1


def _stmts_to_tree2(ast_list:list, lv_list:list, current_line, lv)->(list, int):
    body = []
    current_line += 1
    stmts_kws_list = ['body', 'orelse', 'finalbody']
    # exprs_kws_list = ['returns', 'values', 'targets', 'decorator_list', 'bases'] # expr*
    expr_kws_list = ['returns', 'values', 'targets', 'decorator_list', 'bases', 'return', 'value', 'target', 'iter',
                     'test', 'returns', 'name', 'annotation', 'subject', 'exc', 'cause', 'msg'] # expr?, expr and expr*
    string_kws_list = ['type_comment']

    while True:
        # stmt为空的情况已经能够处理
        if lv_list[current_line] < lv + 1 or current_line > len(lv_list):
            return body, current_line
        elif lv_list[current_line] > lv + 1:
            raise ValueError(f"went wrong at {current_line} when transforming \n"
                             f"line: {ast_list[current_line]}, lv: {lv}, line_lv: {lv_list[current_line]}")
        else:
            stmt_item = ast_list[current_line].strip().strip('()],')
            body_list = []
            current_line += 1
            while lv_list[current_line] == lv + 2:
                kw = ast_list[current_line].strip().split('=')[0]
                if kw in stmts_kws_list:
                    temp_list, current_line = _stmts_to_tree2(ast_list, lv_list, current_line, lv+2)

                    # stmt为空的情况也涵盖在其中
                    body_list.extend(temp_list)
                elif kw in expr_kws_list:
                    temp, current_line = _expr_to_tree(ast_list, lv_list, current_line, lv + 2)
                    body_list.append(temp)
                elif kw in string_kws_list:
                    body_list.append(TreeWithoutParent(ast_list[current_line].split('=')[1].strip(')').strip("'")))
                    current_line += 1
                else:
                    raise ValueError(f'unsupported parameter type {kw}, in stmt {stmt_item}')
            if stmt_item=='Assign':
                stmt_item = '='
            body.append(TreeWithoutParent(stmt_item.lower(), body_list))



def ast_dump_to_tree(ast_dump_str:str) -> TreeWithoutParent:
    ast_list = ast_dump_str.split('\n')
    lv_list = _resolve_level_of_lines(ast_list)
    body, line = _stmts_to_tree2(ast_list, lv_list, 1, 1)
    return  TreeWithoutParent('program', body)




if __name__ == "__main__":
    expected_tree = TreeWithoutParent("program", [
        TreeWithoutParent("while", [
            TreeWithoutParent("!=", [
                TreeWithoutParent("b"),
                TreeWithoutParent("0")
            ]),
            TreeWithoutParent("if", [
                TreeWithoutParent(">", [
                    TreeWithoutParent("a"),
                    TreeWithoutParent("b")
                ]),
                TreeWithoutParent("=", [
                    TreeWithoutParent("a"),
                    TreeWithoutParent("-", [
                        TreeWithoutParent("a"),
                        TreeWithoutParent("b")
                    ])
                ]),
                TreeWithoutParent("=", [
                    TreeWithoutParent("b"),
                    TreeWithoutParent("-", [
                        TreeWithoutParent("b"),
                        TreeWithoutParent("a")
                    ])
                ])
            ])
        ]),
        TreeWithoutParent("return", [
            TreeWithoutParent("a")
        ])
    ])

    source_code = """
        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
    """

    # Remove extra indentation from the source code
    source_code = textwrap.dedent(source_code)
    # Build the AST using the ast module
    tree = ast.parse(source_code)
    ast_string = ast.dump(tree, indent=3)
    # print(ast_string)
    custom_tree = ast_dump_to_tree(ast_string)


    assert trees_equal(expected_tree, custom_tree), "The trees do not match!"
