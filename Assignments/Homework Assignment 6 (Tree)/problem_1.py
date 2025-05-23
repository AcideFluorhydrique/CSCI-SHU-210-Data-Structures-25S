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


def ast_dump_to_tree(ast_dump_str):
    # TODO: Please write your code here

    # def tokenize(s):
    #     """ 换成 list of tokens."""
    #     tokens = []
    #     i = 0
    #     while i < len(s):
    #         if s[i].isalpha():
    #             j = i
    #             while j < len(s) and s[j].isalpha():
    #                 j += 1
    #             tokens.append(s[i:j])
    #             i = j
    #         elif s[i] == "'":
    #             j = i + 1
    #             while j < len(s) and s[j] != "'":
    #                 j += 1
    #             tokens.append(s[i:j + 1])
    #             i = j + 1
    #         elif s[i].isdigit():
    #             j = i
    #             while j < len(s) and s[j].isdigit():
    #                 j += 1
    #             tokens.append(s[i:j])
    #             i = j
    #         elif s[i] in "()[],=":
    #             tokens.append(s[i])
    #             i += 1
    #         elif s[i].isspace():
    #             i += 1
    #         else:
    #             raise ValueError(f"Unexpected character: {s[i]}")
    #     return tokens
    #
    # def parse_value(tokens, i):
    #     """Parse a value, which can be a node, list, or simple value."""
    #     if tokens[i] == "[":
    #         return parse_list(tokens, i)
    #     elif tokens[i].isalpha() and i + 1 < len(tokens) and tokens[i + 1] == "(":
    #         return parse_node(tokens, i)
    #     else:
    #         value = tokens[i]
    #         i += 1
    #         return value, i
    #
    # def parse_list(tokens, i):
    #     """Parse a list enclosed in square brackets."""
    #     if tokens[i] != "[":
    #         raise ValueError("Expected '['")
    #     i += 1
    #     items = []
    #     while tokens[i] != "]":
    #         item, i = parse_value(tokens, i)
    #         items.append(item)
    #         if tokens[i] == ",":
    #             i += 1
    #     i += 1  # Consume "]"
    #     return items, i
    #
    # def parse_node(tokens, i):
    #     """pass"""
    #     node_type = tokens[i]
    #     i += 1
    #     if tokens[i] != "(":
    #         raise ValueError("Expected '('")
    #     i += 1
    #     fields = {}
    #     while tokens[i] != ")":
    #         field_name = tokens[i]
    #         i += 1
    #         if tokens[i] != "=":
    #             raise ValueError("Expected '='")
    #         i += 1
    #         value, i = parse_value(tokens, i)
    #         fields[field_name] = value
    #         if tokens[i] == ",":
    #             i += 1
    #     i += 1  # Consume ")"
    #     return {'type': node_type, 'fields': fields}, i
    #
    # op_map = {
    #     'NotEq': '!=',
    #     'Gt': '>',
    #     'Sub': '-',
    # }
    #
    # def simplify_node(node):
    #     node_type = node['type']
    #     print(f"Simplifying node of type: {node_type}")
    #
    #     if node_type == 'Module':
    #         body = node['fields']['body']
    #         simplified_body = [simplify_node(stmt) for stmt in body]
    #         result = TreeWithoutParent("program", simplified_body)
    #         print(f"Returning for Module: {result}")
    #         return result
    #     elif node_type == 'While':
    #         test = simplify_node(node['fields']['test'])
    #         body = [simplify_node(stmt) for stmt in node['fields']['body']]
    #         result = TreeWithoutParent("while", [test] + body)
    #         print(f"Returning for While: {result}")
    #         return result
    #     elif node_type == 'If':
    #         test = simplify_node(node['fields']['test'])
    #         body = [simplify_node(stmt) for stmt in node['fields']['body']]
    #         orelse = [simplify_node(stmt) for stmt in node['fields']['orelse']]
    #         result = TreeWithoutParent("if", [test] + body + orelse)
    #         print(f"Returning for If: {result}")
    #         return result
    #     elif node_type == 'Return':
    #         value = simplify_node(node['fields']['value'])
    #         result = TreeWithoutParent("return", [value])
    #         print(f"Returning for Return: {result}")
    #         return result
    #     elif node_type == 'Assign':
    #         target = simplify_node(node['fields']['targets'][0])
    #         value = simplify_node(node['fields']['value'])
    #         result = TreeWithoutParent("=", [target, value])
    #         print(f"Returning for Assign: {result}")
    #         return result
    #     elif node_type == 'Compare':
    #         left = simplify_node(node['fields']['left'])
    #         op = node['fields']['ops'][0]['type']
    #         op_str = op_map.get(op, op)  # 假设 op_map 已定义
    #         comparator = simplify_node(node['fields']['comparators'][0])
    #         result = TreeWithoutParent(op_str, [left, comparator])
    #         print(f"Returning for Compare: {result}")
    #         return result
    #     elif node_type == 'BinOp':
    #         left = simplify_node(node['fields']['left'])
    #         op = node['fields']['op']['type']
    #         op_str = op_map.get(op, op)  # 假设 op_map 已定义
    #         right = simplify_node(node['fields']['right'])
    #         result = TreeWithoutParent(op_str, [left, right])
    #         print(f"Returning for BinOp: {result}")
    #         return result
    #     elif node_type == 'Name':
    #         id_str = node['fields']['id'][1:-1]  # 去除引号
    #         result = TreeWithoutParent(id_str)
    #         print(f"Returning for Name: {result}")
    #         return result
    #     elif node_type == 'Constant':
    #         value = node['fields']['value']
    #         result = TreeWithoutParent(value)
    #         print(f"Returning for Constant: {result}")
    #         return result
    #     else:
    #         print(f"Unknown node type: {node_type}")
    #         raise ValueError(f"Unknown node type: {node_type}")
    #     # pass
    #


    ast_list = ast_dump_str.split("\n")

    """
    
    TO Grader, I failed to finish this problem by my self, 
    so I do use ChatGPT and
    I also look at Paul Huang(zh2919@nyu.edu)'s assignment code, 
    https://en.wikipedia.org/wiki/Abstract_syntax_tree
    ,and follow Python's document https://docs.python.org/zh-cn/3.13/library/ast.html
    
    as references
    
    """

    lv_list = [

    ]
    for line in ast_list:
        num_of_space = len(line) - len(line.strip())
        lv = num_of_space // 3
        if num_of_space != lv * 3:
            raise SyntaxError("can't resolve input: wrong indention")
        lv_list.append(lv)

    # 整合 extract_outermost_parentheses 的逻辑
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
                        return text[start:i + 1]
        return None

    # 整合 _expr_to_tree 的逻辑
    def parse_expr(ast_list, lv_list, current_line, lv):
        operator_mapping = {
            "And": "and", "Or": "or", "Add": "+",
            "Sub": "-", "Mult": "*", "MatMult": "@",
            "Div": "/", "Mod": "%", "Pow": "**",
            "LShift": "<<", "RShift": ">>", "BitOr": "|",
            "BitXor": "^", "BitAnd": "&", "FloorDiv": "//",
            "Invert": "~", "Not": "not",
            "UAdd": "+", "USub": "-", "Eq": "==",
            "NotEq": "!=", "Lt": "<", "LtE": "<=",
            "Gt": ">", "GtE": ">=", "Is": "is",
            "IsNot": "is not", "In": "in", "NotIn": "not in"
        }

        op_kws_list = [
            "op",
            "ops",
        ]
        expr_kws_list = [
            'values', 'target', 'value',
            'left', 'right', 'operand',
            'body', 'test', 'orelse',
            'keys', 'elts', 'elt', 'key',
            'comparators', 'func', 'args',
            'format_spec', 'slice',
        ]

        idf_kws_list = [
            "attr",
            "id",
        ]
        params = []
        root = None

        if (current_line + 1 >= len(lv_list) or
                lv_list[current_line + 1] <= lv
        ):  # 单行表达式

            match = extract_outermost_parentheses(ast_list[current_line])
            if match:
                try:
                    param_list = match.split(',')
                except AttributeError as e:
                    print(f"line: {current_line}, line_str: {ast_list[current_line]}\n"
                          f"exception info: {e}"
                    )
                    sys.exit(1)
                current_line += 1
                for param in param_list:
                    if 'id' in param:
                        return TreeWithoutParent(
                            param.strip('[]() ').split('=')[1].strip("'\"")
                        ), current_line
                    elif 'value' in param:
                        return TreeWithoutParent(
                            param.strip('[]() ').split('=')[1].strip("'\"")
                        ), current_line
                raise ValueError(f'met unsupported parameter for expr in line {current_line}\n'
                                 f'line info: {ast_list[current_line]}'
                )
            else:
                raise ValueError(f'failed to extract parentheses in line {current_line}\n'
                                 f'line info: {ast_list[current_line]}'
                )
        else:  # 多行表达式
            current_line += 1
            while True:
                if (current_line >= len(lv_list) or
                        lv_list[current_line] < lv + 1
                ):
                    if root:
                        root._children = params
                        return root, current_line
                    elif len(params) == 1:
                        return params[0], current_line
                    else:
                        raise ValueError(f"went wrong at line {current_line} when transforming. \n"
                                         f"line information {ast_list[current_line]}\n"
                                         f"Can't find a root node among {[node._element for node in params]}"
                        )
                elif lv_list[current_line] > lv + 1:
                    raise ValueError(f"went wrong at line {current_line} when transforming. \n"
                                     f"line information {ast_list[current_line]}\n"
                    )
                else:
                    expr_item = ast_list[current_line].split("=")[0].strip().split('(')[-1]
                    if expr_item in expr_kws_list:
                        node, current_line = parse_expr(ast_list, lv_list, current_line, lv + 1)
                        params.append(node)
                    elif expr_item in op_kws_list:
                        if lv_list[current_line + 1] <= lv_list[current_line]:  # 单行
                            op_str = ast_list[current_line].split('=')[1].strip('[](), ')
                            root = TreeWithoutParent(operator_mapping[op_str])
                            current_line += 1
                        else:  # 多行
                            current_line += 1
                            op_str = ast_list[current_line].strip('[](), ')
                            root = TreeWithoutParent(operator_mapping[op_str])
                            current_line += 1
                    elif expr_item in idf_kws_list:
                        var = ast_list[current_line].split('\'')[1]
                        params.append(TreeWithoutParent(var))
                        current_line += 1
                    else:
                        current_line += 1
                        print(f'met unsupported expr_item {expr_item} in line {current_line}\n'
                              f'line info: {ast_list[current_line]}'
                        )
                        while current_line < len(lv_list) and lv_list[current_line] > lv + 1:
                            current_line += 1

    # 整合 _stmts_to_tree2 的逻辑
    def parse_stmts(ast_list, lv_list, current_line, lv):
        body = []
        current_line += 1
        stmts_kws_list = [
            'body',
            'orelse',
            'finalbody',
        ]
        expr_kws_list = [
            'returns', 'values', 'targets',
            'decorator_list', 'bases', 'return',
            'value', 'target',
            'iter', 'test', 'returns', 'name',
            'annotation', 'subject', 'exc',
            'cause', 'msg',
        ]
        string_kws_list = ["type_comment"]

        while True:
            if current_line >= len(lv_list) or lv_list[current_line] < lv + 1:
                return body, current_line
            elif lv_list[current_line] > lv + 1:
                raise ValueError(f"went wrong at {current_line} when transforming \n"
                                 f"line: {ast_list[current_line]}, lv: {lv}, line_lv: {lv_list[current_line]}"
                )
            else:
                stmt_item = ast_list[current_line].strip().strip('()],')
                body_list = []
                current_line += 1
                while current_line < len(lv_list) and lv_list[current_line] == lv + 2:
                    kw = ast_list[current_line].strip().split('=')[0]
                    if kw in stmts_kws_list:
                        temp_list, current_line = parse_stmts(ast_list, lv_list, current_line, lv + 2)
                        body_list.extend(temp_list)
                    elif kw in expr_kws_list:
                        temp, current_line = parse_expr(ast_list, lv_list, current_line, lv + 2)
                        body_list.append(temp)
                    elif kw in string_kws_list:
                        body_list.append(
                            TreeWithoutParent(ast_list[current_line].split('=')[1].strip(')').strip("'"))
                        )
                        current_line += 1
                    else:
                        raise ValueError(f'unsupported parameter type {kw}, in stmt {stmt_item}')
                if stmt_item == 'Assign':
                    stmt_item = '='
                body.append(TreeWithoutParent(stmt_item.lower(), body_list))

    # 主逻辑
    body, line = parse_stmts(ast_list, lv_list, 1, 1)
    return TreeWithoutParent('program', body)
    # pass


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
    custom_tree = ast_dump_to_tree(ast_string)
    custom_tree.pretty_print()

    assert trees_equal(expected_tree, custom_tree), "The trees do not match!"
