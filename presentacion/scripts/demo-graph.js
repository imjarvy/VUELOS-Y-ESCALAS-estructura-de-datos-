import { createGraphUi, transformAirportsToGraphData } from "./graphUI.js";

const status = document.getElementById("status");

const graphUi = createGraphUi({
  state: { selectedCode: null },
  onNodeSelect: node => {
    status.textContent = `Seleccionado: ${node.id} | ${node.name ?? node.city ?? "Sin nombre"}`;
  },
});

async function loadAndRenderSample() {
  status.textContent = "Cargando sample-airports.json...";

  try {
    const response = await fetch("../../sample-airports.json");
    if (!response.ok) {
      throw new Error("No se pudo leer sample-airports.json");
    }

    const airports = await response.json();
    const graphData = transformAirportsToGraphData(airports);

    graphUi.renderGraph(graphData, "graphSvg", "graphContainer");

    status.textContent = `Render OK | Aeropuertos: ${graphData.nodes.length} | Rutas: ${graphData.links.length}`;
  } catch (error) {
    status.textContent = `Error: ${error.message}`;
    console.error(error);
  }
}

document.getElementById("btnLoadSample").addEventListener("click", loadAndRenderSample);

loadAndRenderSample();