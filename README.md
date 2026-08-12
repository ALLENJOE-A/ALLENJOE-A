<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=header&text=ALLEN%20JOE%20A&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=VLSI%20Engineer%20%E2%80%A2%20Semiconductor%20Devices%20%E2%80%A2%20Embedded%20Systems&descAlignY=60&descSize=16" width="100%" />

<p>
  <img src="https://img.shields.io/badge/VLSI_Design-101010?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDJMMiA3bDEwIDUgMTAtNXptMCA0TDYgOWw2IDMgNi0zeiIvPjwvc3ZnPg==&logoColor=blueviolet&color=0D1117" />
  <img src="https://img.shields.io/badge/RTL_Development-101010?style=for-the-badge&logo=electron&logoColor=00D9FF&color=0D1117" />
  <img src="https://img.shields.io/badge/Embedded_Systems-101010?style=for-the-badge&logo=stmicroelectronics&logoColor=FF6B6B&color=0D1117" />
  <img src="https://img.shields.io/badge/AI_for_EDA-101010?style=for-the-badge&logo=pytorch&logoColor=4ECDC4&color=0D1117" />
</p>

</div>

---

## 👨‍💻 About Me

Electronics & VLSI Engineering at VIT Chennai. Bridging the gap between hardware architecture, computational lithography, and practical embedded systems. My work focuses on semiconductor modeling, high-performance RTL design, and geometric deep learning for computational lithography.

**🔬 Current Engineering Focus:**
* **Computational EDA:** Applying Equivariant Graph Neural Networks (EGNN) and Graph Transformers to Edge-Placement-Error (EPE) prediction.
* **Semiconductor Device Modeling:** Optimization of advanced node devices (e.g., Vertical TFETs) using TCAD.
* **Embedded Instrumentation:** Developing real-time signal acquisition and visualization architectures on ARM Cortex-M.

---

## 🛠️ Technical Expertise

### Hardware / VLSI
`RTL Design` `Digital Logic Design` `Cascode Architectures` `Semiconductor Physics` `Device Characterization` `Small Signal Analysis`

### AI / ML for EDA
`Equivariant Graph Neural Networks (EGNN)` `Graph Transformers` `Multi-Task Uncertainty Weighting` `PyTorch` `PyTorch Geometric`

### Programming & Embedded
`Python` `Embedded C` `C/C++` `ARM Assembly` `STM32 / Cortex-M3` `ADC + DMA Acquisition` `SPI / TFT Interfacing`

### EDA & Simulation Tools
`Synopsys Sentaurus TCAD` `LTspice` `Verilog/SystemVerilog`

---

## 🚀 Engineering Work & Featured Projects

<details open>
<summary><b>GNN-T: Edge-Error Prediction for Computational Lithography</b></summary>

> **Research Prototype:** Equivariant graph learning architecture combining EGNNs and Graph Transformers to predict post-OPC mask deviations and edge placement errors in computational lithography.

* **Problem:** Traditional rigorous lithography simulation is computationally expensive.
* **Architecture:** Radius-graph construction over layout polygons, EGNN coordinate processing, and a multi-head scalar Graph Transformer.
* **Innovation:** Multi-task uncertainty weighting across 5 distinct predictive regression/classification heads (`F_x`, `F_y`, `F_z`, `Metric Distortion`, `Instability`).
* **Tech Stack:** `Python`, `PyTorch`, `PyTorch Geometric`, `EGNN`, `Graph Transformer`
* **Link:** [GNN-T_Edge-Error-Prediction-for-Computational-Lithography](https://github.com/ALLENJOE-A/GNN-T_Edge-Error-Prediction-for-Computational-Lithography)
</details>

<details>
<summary><b>Pocket-Engineered Vertical TFET Design</b></summary>

> **Device Simulation:** Advanced semiconductor device modeling project exploring short-channel effect mitigation in Vertical Tunnel FETs (VTFET).

* **Problem:** Subthreshold swing constraints in classical MOSFETs scaling.
* **Approach:** DG-Source-Pocket engineering to optimize band-to-band tunneling (BTBT) rates.
* **Result:** Device physics characterization and performance optimization modeling.
* **Tech Stack:** `Synopsys Sentaurus TCAD`, `Device Modeling`, `Semiconductor Physics`
* **Link:** [DG-Source-Pocket-Engineered-Vertical-TFET](https://github.com/ALLENJOE-A/DG-Source-Pocket-Engineered-Vertical-TFET)
</details>

<details>
<summary><b>ARM Cortex-M Digital Oscilloscope</b></summary>

> **Embedded Instrumentation:** Portable Digital Storage Oscilloscope (DSO) achieving ~857 kSa/s real-time waveform acquisition on an STM32.

* **Architecture:** Analog Front-End (AFE) -> STM32F103 12-bit ADC -> DMA Circular Buffer -> Software Edge Triggering -> SPI TFT Display.
* **Implementation:** Pure bare-metal/HAL C implementation bypassing dedicated FPGA acquisition hardware for a low-cost embedded solution.
* **Tech Stack:** `Embedded C`, `STM32`, `DMA`, `ILI9341 SPI`, `Signal Processing`
* **Link:** [Digital-Oscilloscope-STM32](https://github.com/ALLENJOE-A/Digital-Oscilloscope-STM32)
</details>

<details>
<summary><b>Cascode Differential Amplifier</b></summary>

> **Analog IC Design:** Wide-swing high-gain analog design modeled and simulated in LTspice.

* **Focus:** MOSFET cascode architecture designed for high-gain differential amplification and optimized output swing.
* **Tech Stack:** `LTspice`, `Analog Design`, `Circuit Analysis`
</details>

---

## 🗺️ Knowledge Map

```text
Computational EDA
      ↓
Equivariant GNNs → Graph Transformers → Edge Error Prediction

Semiconductor Devices
      ↓
TCAD Modeling → Vertical TFETs → Band-to-Band Tunneling (BTBT)

Embedded Instrumentation
      ↓
Analog Front-End → Cortex-M3 (ADC+DMA) → SPI Graphics Processing
```

---

## 📊 GitHub Analytics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=ALLENJOE-A&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&icon_color=00D9FF&text_color=FFFFFF&count_private=true&include_all_commits=true" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ALLENJOE-A&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&text_color=FFFFFF" width="48%" />
</div>

---

## 🌐 Connect With Me

* **GitHub:** [@ALLENJOE-A](https://github.com/ALLENJOE-A)
* **LinkedIn:** [Allen Joe A](https://www.linkedin.com/in/allen-joe-a-36069831b/)
* **Email:** [allenjoe.a2024@vitstudent.ac.in](mailto:allenjoe.a2024@vitstudent.ac.in)

<div align="center">
  <sub>Building the future of computing, one transistor and graph at a time.</sub>
</div>
