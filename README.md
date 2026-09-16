<div align="center">

<!-- Die-shot / reticle header banner -->
<img src="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/main/assets/header-die-shot.svg" width="100%" alt="Allen Joe A - VLSI Engineer | Chip Designer | RTL Developer"/>

<!-- Typing Animation Effect -->
<a href="https://readme-typing-svg.demolab.com"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=100&lines=ASIC+Physical+Design+%7C+RTL+Design;TCAD+%2F+Device+Modeling+%7C+GNN+Research;Functional+Verification+%7C+Embedded+Systems" alt="Typing SVG" /></a>

</div>

<br/>

## About Me

```verilog
// ──────────────────────────────────────────────────────────────
//  Module:  allen_joe_engineer
//  Author:  Allen Joe A
//  Rev:     1.0  |  VIT Chennai Foundry
// ──────────────────────────────────────────────────────────────

module allen_joe_engineer #(
  parameter  NAME           = "Allen Joe A",
  parameter  LOCATION       = "Chennai, India",
  parameter  INSTITUTION    = "VIT Chennai",
  parameter  DEGREE         = "Electronics & VLSI Engineering"
)(
  input  wire        clk,
  input  wire        rst_n,
  output reg  [7:0]  innovation
);

  // ── Internal Signals ──────────────────────────────────────
  wire  asic_physical_design;    // Floorplan → Tapeout
  wire  rtl_design;              // Verilog / SystemVerilog
  wire  functional_verification; // SVA, UVM, Coverage
  wire  tcad_device_modeling;    // Sentaurus TCAD, VTFET/FinFET
  wire  gnn_litho_research;     // GNN+Transformer EPE prediction
  wire  embedded_systems;        // STM32, FPGA, ADC/DMA

  // ── Combinational Logic ───────────────────────────────────
  assign innovation = {asic_physical_design,
                       rtl_design,
                       functional_verification,
                       tcad_device_modeling,
                       gnn_litho_research,
                       embedded_systems,
                       2'b11};  // always learning

  // ── Sequential — never stops ──────────────────────────────
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      innovation <= 8'h00;
    else
      innovation <= innovation + 1'b1;  // continuous growth
  end

endmodule
```

<br/>

## Chip Floorplan &#x2014; Skills & Expertise

<div align="center">

<img src="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/main/assets/floorplan-skills.svg" width="100%" alt="Chip Floorplan - Skills & Expertise Diagram"/>

</div>

<br/>

## Tools & Technologies &#x2014; Timing Diagram

<div align="center">

<img src="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/main/assets/timing-diagram-tools.svg" width="100%" alt="Tools Proficiency - Timing Diagram"/>

</div>

<br/>

## Tape-Out Log &#x2014; Featured Projects

```
╔═══════════╦══════════════════════════════════════════════════╦══════════════════════╦════════════════╦══════════════════════════════╗
║  LOT_ID   ║  PROJECT                                         ║  DOMAIN              ║  STATUS        ║  STACK                       ║
╠═══════════╬══════════════════════════════════════════════════╬══════════════════════╬════════════════╬══════════════════════════════╣
║  AJA-001  ║  DG-Source-Pocket-Engineered-Vertical-TFET       ║  TCAD / Device Sim   ║  ■ TAPED OUT   ║  Sentaurus TCAD, Batchfile   ║
║  AJA-002  ║  Digital-Oscilloscope-STM32                      ║  Embedded Systems    ║  ■ TAPED OUT   ║  STM32, C, ADC+DMA, ILI9341  ║
║  AJA-003  ║  GNN-T_Edge-Error-Prediction-Lithography         ║  ML / Comp. Litho    ║  ■ TAPED OUT   ║  Python, PyTorch, GNN+Trans   ║
║  AJA-004  ║  Cascode Differential Amplifier                  ║  Analog / Mixed-Sig  ║  □ IN DESIGN   ║  LTspice, MOSFET, Op-Amp     ║
╚═══════════╩══════════════════════════════════════════════════╩══════════════════════╩════════════════╩══════════════════════════════╝
```

> **Repo Links:**
> [`AJA-001`](https://github.com/ALLENJOE-A/DG-Source-Pocket-Engineered-Vertical-TFET) &#x2022;
> [`AJA-002`](https://github.com/ALLENJOE-A/Digital-Oscilloscope-STM32) &#x2022;
> [`AJA-003`](https://github.com/ALLENJOE-A/GNN-T_Edge-Error-Prediction-for-Computational-Lithography) &#x2022;
> `AJA-004` *(repo coming soon)*

<br/>

## GitHub Statistics

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=ALLENJOE-A&show_icons=true&hide_border=true&bg_color=0D1117&title_color=00D9FF&icon_color=00FF88&text_color=8899AA&ring_color=00D9FF&count_private=true&include_all_commits=true" />
<img width="40%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ALLENJOE-A&layout=compact&hide_border=true&bg_color=0D1117&title_color=00D9FF&text_color=8899AA&langs_count=8" />

</div>

<br/>

## Contribution Activity

Real-time contribution data &#x2014; all graphs auto-update from live GitHub activity.

<div align="center">

<!-- Streak Stats -->
<img width="60%" src="https://github-readme-streak-stats.herokuapp.com/?user=ALLENJOE-A&hide_border=true&background=0D1117&stroke=1A3A4A&ring=00D9FF&fire=FF6B6B&currStreakNum=FFFFFF&sideNums=00D9FF&currStreakLabel=00D9FF&sideLabels=8899AA&dates=3A5A6A" />

<br/><br/>

<!-- Activity Graph (last 31 days) -->
<img width="95%" src="https://github-readme-activity-graph-xi.vercel.app/graph?username=ALLENJOE-A&bg_color=0D1117&color=8899AA&line=00D9FF&point=00FF88&area_color=00D9FF&area=true&hide_border=true&custom_title=Commit%20Activity%20(Last%2031%20Days)&title_color=00D9FF" alt="GitHub Activity Graph"/>

<br/><br/>

<!-- Snake Contribution Grid Animation -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/output/github-contribution-grid-snake.svg" />
  <img alt="Snake animation" src="https://raw.githubusercontent.com/ALLENJOE-A/ALLENJOE-A/output/github-contribution-grid-snake-dark.svg" />
</picture>

</div>

<br/>

## Connect

<div align="center">

<a href="https://github.com/ALLENJOE-A">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</a>
<a href="https://www.linkedin.com/in/allenjoe-a" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="mailto:allenjoe.a2024@vitstudent.ac.in">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=ALLENJOE-A&style=flat-square&color=00D9FF&label=Profile+Views" alt="Profile Views" />

</div>
