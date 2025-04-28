
import React from "react"
import * as d3 from "d3"


const csvUrl = "https://gist.githubusercontent.com/hogwild/4a23b2327e88e6e3aa101bb01ddb28ba/raw/81fd842af7328d2ad6d2a498cc4589031ae5b4af/citibike_rawdata_2020_4.csv"

function useData(csvPath){
    const [dataAll, setData] = React.useState(null);
    React.useEffect(() => {
        d3.csv(csvPath).then(data => {
            setData(data);
        });
    }, []);
    return dataAll;
}

function Graph(props) {
    const { x, y, width, height, data } = props;
    const d3Selection = React.useRef();
    React.useEffect( ()=>{
        let nodes = d3.groups(data, d => d["end station id"])
            .map( d => {return {id: d[0], name: d[1][0]["end station name"], value:d[1].length}});
        // console.log(nodes);
        const radius = d3.scaleLinear().range([1, 100])
            .domain([d3.min(nodes, d => d.value), d3.max(nodes, d => d.value)]);
        
        const color = (id) => {
            const n = +id[1];
            return d3.schemeCategory10[n];
        };

        const simulation =  d3.forceSimulation(nodes)
            .velocityDecay(0.2)
            .force("x", d3.forceX([width/2]).strength(0.02))
            .force("y", d3.forceY([height/2]).strength(0.02))
            .force("collide", d3.forceCollide().radius(d => radius(d.value)))
            .force("charge", d3.forceManyBody())
            .force("centrer", d3.forceCenter( width/2, height/2));
        
        let g = d3.select(d3Selection.current)

        const node = g.append("g")
            .attr("stroke", "#fff")
            .attr("stroke-width", 1.5)
            .selectAll("circle")
            .data(nodes)
            .enter()
        const point = node.append("circle")
            .attr("r", d => radius(d.value))
            .attr("fill", d => color(d.id))
            .call(drag(simulation));
        
        const node_text = node.append('text')
                    .style("fill", "black")
                    .attr("stroke", "black")
                    .text(d => d.name)
                    
            
        simulation.on("tick", () => {
            point
                .attr("cx", d => d.x)
                .attr("cy", d => d.y)
            node_text
                .attr("x", d => d.x-radius(d.value)/2)
                .attr("y", d => d.y)
                
        });
        function drag (simulation){
            function dragstarted(event) {
                // console.log(event.subject);
                if (!event.active) simulation.alphaTarget(0.3).restart();
                event.subject.fx = event.subject.x;
                event.subject.fy = event.subject.y;
            }
            function dragged(event) {
                event.subject.fx = event.x;
                event.subject.fy = event.y;
            }
            function dragended(event) {
                if (!event.active) simulation.alphaTarget(0);
                event.subject.fx = null;
                event.subject.fy = null;
            }
            return d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended);
        };
    }, [width, height])
    return <g ref={d3Selection} transform={`translate(${x}, ${y})`}>
        </g>
};
const ForceCllideGraph = () => {
    const WIDTH = 800;
    const HEIGHT = 800;
    const margin = { top: 20, right: 40, bottom: 20, left: 40 };
    const width = WIDTH - margin.left - margin.right;
    const height = HEIGHT - margin.top - margin.bottom;
    const rawData = useData(csvUrl);
    if (!rawData) {
        return <p>Loading...</p>
    }
    
    return (
        <>
        <h1>Citi Bike Station Popularity</h1>
        <svg width={WIDTH} height={HEIGHT}>
            <Graph x={margin.left} y={margin.right} width={width} height={height} data={rawData}/>
        </svg>
        </>)
}

export default ForceCllideGraph