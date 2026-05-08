import { apiPostFormData } from "./api/client.js";
import { createGraphUi, transformGraphToD3Data } from "./graphUI.js";

const status = document.getElementById("status");
const jsonModal = document.getElementById("jsonModal");
const jsonFileInput = document.getElementById("jsonFile");
const fileLabel = document.getElementById("fileLabel");

function openModal() {
  jsonModal.classList.remove("hidden");
}

function closeModal() {
  jsonModal.classList.add("hidden");
}

const graphUi = createGraphUi({
  state: { selectedCode: null },
  onNodeSelect: node => {
    status.textContent = `Seleccionado: ${node.id} | ${node.name ?? node.city ?? "Sin nombre"}`;
  },
});

jsonFileInput.addEventListener("change", event => {
  const selectedFile = event.target.files?.[0];
  fileLabel.textContent = selectedFile ? `📂 ${selectedFile.name}` : "Seleccionar archivo .json";
});

document.querySelectorAll(".modal-close[data-close]").forEach(button => {
  button.addEventListener("click", () => closeModal());
});

jsonModal.addEventListener("click", event => {
  if (event.target === jsonModal) closeModal();
});

document.getElementById("btnLoadSample").addEventListener("click", openModal);

document.getElementById("loadJsonConfirmBtn").addEventListener("click", async () => {
  const file = jsonFileInput.files?.[0];
  if (!file) {
    status.textContent = "Selecciona un archivo JSON primero.";
    return;
  }

  status.textContent = "Cargando JSON...";
  
  const formData = new FormData();
  formData.append("file", file);
  
  const response = await apiPostFormData("/api/load-graph", formData);
  const d3Graph = transformGraphToD3Data(response.graph ?? response);

  graphUi.renderGraph(d3Graph, "graphSvg", "graphContainer");
  status.textContent = `Grafo cargado: ${response.airports ?? d3Graph.nodes.length} aeropuertos.`;
  closeModal();
});