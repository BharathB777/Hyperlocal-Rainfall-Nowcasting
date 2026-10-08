# -*- coding: utf-8 -*-
"""
Exhaustive Knowledge Graph Generator for 'Multi-Source AI for Hyperlocal Rainfall Nowcasting'
Builds a 100% complete, fully articulated graph.json conforming to Graphify / NetworkX specifications.
Contains all academic metadata, literature survey papers, mathematical formulations,
code files, database schemas, 15 implementation steps, evaluation metrics, empirical results,
PPT review decks, demo walkthrough steps, and 20 viva voce Q&As.
"""

import json
import sys
from pathlib import Path

def build_exhaustive_knowledge_graph():
    graph_data = {
        "directed": True,
        "multigraph": False,
        "graph": {
            "name": "Multi-Source AI for Hyperlocal Rainfall Nowcasting Knowledge Graph",
            "version": "2.0.0",
            "generated_tool": "Graphify",
            "repository": "d:/FYP-1",
            "project_title": "Multi-Source AI for Hyperlocal Rainfall Nowcasting",
            "phase": "Phase 1 Completed / Phase 2 Planned",
            "academic_degree": "Bachelor of Technology (B.Tech) - Computer Science and Engineering",
            "institution": "Sri Manakula Vinayagar Engineering College (SMVEC), Madagadipet, Puducherry - 605107",
            "affiliation": "Pondicherry University",
            "academic_year": "2026-2027 (Review & Submission: October 2026)",
            "team_members": [
                {"name": "Ariyan M", "register_no": "23UCS015", "role": "Full-Stack Architecture & Data Ingestion"},
                {"name": "Bharath B", "register_no": "23UCS025", "role": "Deep Learning Pipeline & Model Design"},
                {"name": "Hemnnath G", "register_no": "23UCS066", "role": "Feature Engineering & Frontend Dashboard"}
            ],
            "project_guide": "Dr. N. Danapaquiame (Professor and Head of the Department, CSE, SMVEC)",
            "director_principal": "Dr. V. S. K. Venkatachalapathy",
            "chairman_md": "Shri. M. Dhanasekaran",
            "description": "Exhaustive full-stack AI and meteorological knowledge graph combining multi-source data ingestion (IMD AWS, Ambient PWS, Open-Meteo), deep learning precipitation nowcasting (LSTMAtU-Net base paper + proposed TransAtU-Net extension with ECSA attention), multi-model NWP blend guidance, 15 implementation steps, empirical evaluation benchmarks, and an interactive Next.js dashboard."
        },
        "nodes": [],
        "links": [],
        "hyperedges": []
    }

    nodes = []
    links = []

    def add_node(node_id, label, node_type, community_id, community_name, summary, details, file_path=None, metadata=None):
        node = {
            "id": node_id,
            "label": label,
            "type": node_type,
            "community": community_id,
            "community_name": community_name,
            "summary": summary,
            "body": details,
            "norm_label": label.lower()
        }
        if file_path:
            node["file_path"] = file_path
        if metadata:
            node["metadata"] = metadata
        nodes.append(node)

    def add_edge(source, target, relation, label, description=None, weight=1.0):
        link = {
            "source": source,
            "target": target,
            "relation": relation,
            "label": label,
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "weight": weight
        }
        if description:
            link["description"] = description
        links.append(link)

    # =========================================================================
    # COMMUNITY 0: Project Academic Profile, Team & Accreditation
    # =========================================================================
    add_node(
        node_id="project_academic_meta",
        label="Project Academic Profile & Team Credentials",
        node_type="academic_profile",
        community_id=0,
        community_name="Project Overview & Academic Profile",
        summary="Official academic metadata for B.Tech CSE Final Year Project at SMVEC Puducherry.",
        details=r"""# Project Academic Profile
- **Project Title**: Multi-Source AI for Hyperlocal Rainfall Nowcasting
- **Phase**: Project Report — Phase 1 Completed / Phase 2 Planned
- **Degree**: Bachelor of Technology (B.Tech) in Computer Science and Engineering
- **Department**: Department of Computer Science and Engineering
- **Institution**: Sri Manakula Vinayagar Engineering College (SMVEC), Madagadipet, Puducherry - 605107
- **Affiliation**: Affiliated to Pondicherry University
- **Academic Year**: 2026–2027 (Review & Submission: October 2026)

## Student Project Team
1. **Ariyan M** — Register No.: 23UCS015 (CSE)
2. **Bharath B** — Register No.: 23UCS025 (CSE)
3. **Hemnnath G** — Register No.: 23UCS066 (CSE)

## Project Guide & Leadership
- **Project Guide & HOD**: Dr. N. Danapaquiame, Professor and Head of the Department, CSE, SMVEC.
- **Director cum Principal**: Dr. V. S. K. Venkatachalapathy
- **Chairman & Managing Director**: Shri. M. Dhanasekaran
- **Secretary**: Dr. K. Narayanasamy
- **Treasurer**: Shri. D. Rajarajan
- **Joint Secretary**: Shri. S. Velayudham

## Project Abstract
Rainfall forecasting plays an indispensable role in agriculture, transportation, disaster management, and urban flooding prevention. However, conventional Numerical Weather Prediction (NWP) models operate on coarse spatial (10–25 km) and temporal (6–12 h) resolutions, failing to capture rapid localized convective rain events (0–3 hour nowcasting). This project builds a unified weather intelligence platform that:
1. Ingests heterogeneous real-time observations from IMD AWS, community Personal Weather Stations (PWS), and Open-Meteo.
2. Cleans, aligns, and persists data into an asynchronous database.
3. Engineers predictive thermodynamic features (pressure trends, humidity gradients, dew point spread).
4. Implements state-of-the-art deep learning models: base paper **LSTMAtU-Net** (Sensors 2023) and proposed **TransAtU-Net** (Spatio-Temporal Transformer) for 0–2h and 0–3h quantitative precipitation nowcasting.
5. Replicates the ChennaiRains multi-model rainfall blend (ECMWF, GFS, ICON, NCUM, AI) across 20 districts.
6. Delivers a responsive, dark-mode Next.js 16 web dashboard with live telemetry and interactive charts.""",
        file_path="Bharath B - FYP Report.docx",
        metadata={
            "degree": "B.Tech CSE",
            "college": "Sri Manakula Vinayagar Engineering College",
            "university": "Pondicherry University",
            "submission_date": "October 2026"
        }
    )

    add_node(
        node_id="po_pso_curriculum_mapping",
        label="NBA Program Outcomes (PO1-PO12) & PSO Mapping",
        node_type="academic_curriculum",
        community_id=0,
        community_name="Project Overview & Academic Profile",
        summary="Detailed mapping of project components to NBA Program Outcomes and Program Specific Outcomes.",
        details=r"""# Program Outcomes (PO) and PSO Mapping

- **PO1 (Engineering Knowledge)**: Applied meteorological thermodynamics (Magnus-Tetens dew point spread, barometric tendencies), signal processing, and deep learning neural architectures.
- **PO2 (Problem Analysis)**: Formulated the technical gap of coarse NWP models (10-25 km) during Northeast Monsoon convective flash downpours in coastal Tamil Nadu and Puducherry.
- **PO3 (Design/Development of Solutions)**: Designed an end-to-end full-stack weather intelligence platform: asynchronous FastAPI backend, APScheduler ingestion engine, PyTorch ML models, and Next.js 16 web app.
- **PO4 (Conduct Investigations of Complex Problems)**: Benchmarked ConvLSTM, LSTMAtU-Net, and TransAtU-Net models using meteorological metrics (CSI, POD, FAR, HSS) under severe class imbalance.
- **PO5 (Modern Tool Usage)**: PyTorch, FastAPI, Next.js 16, React 19, Tailwind CSS v4, SQLAlchemy Async, Recharts, Leaflet, SQLite, Git, Docker.
- **PO6 (The Engineer and Society)**: Early warning system for urban flooding, traffic disruptions, and squalls in Chennai, Puducherry, and Cuddalore.
- **PO7 (Environment and Sustainability)**: Microclimate tracking for agriculture, water resource conservation, and climate resilience in the Puducherry-Auroville coastal biosphere.
- **PO8 (Ethics)**: Open-source community station attribution, data privacy, and ethical disaster intelligence dissemination.
- **PO9 (Individual and Team Work)**: Collaborative division of responsibilities across full-stack backend, deep learning modeling, and frontend UI design.
- **PO10 (Communication)**: Project documentation, technical PPT reviews, viva defense, and interactive web visualization.
- **PO11 (Project Management and Finance)**: Open-source zero-cost infrastructure deployment using free APIs, local edge compute, and SQLite/PostgreSQL.
- **PO12 (Life-long Learning)**: Keeping pace with advanced AI research (transforming from ConvLSTM to Spatio-Temporal Transformers).
- **PSO1 (Software Development)**: Production-grade asynchronous REST APIs, real-time data streaming, and reactive frontend dashboards.
- **PSO2 (Data Science & Intelligent Systems)**: Time-series feature engineering, multi-source data fusion, and meteorological nowcasting algorithms.""",
        file_path="Multi_Source_AI_PO_PSO_Mapping.pdf"
    )

    add_node(
        node_id="system_specifications_hardware_software",
        label="System Requirements & Hardware/Software Specifications (Chapter 4)",
        node_type="system_specifications",
        community_id=0,
        community_name="Project Overview & Academic Profile",
        summary="Complete hardware, software, runtime, and dependency requirements from Chapter 4 of the project report.",
        details=r"""# System Requirements (Chapter 4)

## Software Requirements:
- **Operating System**: Windows 10/11 (Development) / Ubuntu 22.04 LTS Linux (Production Deployment).
- **Languages**: Python 3.11–3.13 (Backend & ML) | TypeScript 5.0+ / JavaScript ES2024 (Frontend).
- **Frontend Framework**: Next.js 16.3.1 (App Router, Turbopack) | React 19.2.8.
- **Styling & UI**: Tailwind CSS v4 | Lucide React | Recharts 3.10.1 (Data Visualization) | Leaflet (Planned GIS).
- **Backend Framework**: FastAPI 0.120.2 | Uvicorn 0.52.3 (ASGI) | Pydantic 2.12.3 & pydantic-settings.
- **Task Scheduling**: APScheduler 3.10+ (AsyncIOScheduler running in-process).
- **Database Layer**: SQLite 3 (via aiosqlite 0.20+) for local dev | PostgreSQL 16 + TimescaleDB (Production) | SQLAlchemy 2.0.52 (Async ORM).
- **Machine Learning & Deep Learning**: PyTorch 2.7.1 | torchvision | scikit-learn 1.7.2 | XGBoost 3.2.0 | NumPy 2.2.6 | Pandas 2.3.1.
- **NWP & Meteorological GIS**: xarray 2025.7.1 | cfgrib | rasterio | Cartopy 0.24.1 | Matplotlib 3.10.3 | netCDF4 1.7.2.
- **HTTP Client**: HTTPX 0.28.1 (Asynchronous REST API queries).
- **Authentication (Phase 2)**: NextAuth.js | Firebase Authentication (Google & Facebook OAuth).

## Hardware Requirements:
- **Processor**: Intel Core i5/i7 (8th Gen+) or AMD Ryzen 5/7 (6+ physical cores).
- **RAM**: Minimum 16 GB DDR4/DDR5 (for loading multidimensional NWP arrays and training batches).
- **Storage**: Minimum 50 GB SSD storage (for SQLite/TimescaleDB time-series and model checkpoints).
- **GPU (ML Training)**: NVIDIA GeForce RTX 3060 / 4060 (6GB+ VRAM) or Google Colab / Kaggle T4/A100 GPUs for deep learning training.""",
        file_path="Bharath B - FYP Report.docx"
    )

    # =========================================================================
    # COMMUNITY 1: Problem Statement, Research Scope & Literature Survey
    # =========================================================================
    add_node(
        node_id="problem_statement_and_motivation",
        label="Problem Statement & Meteorological Challenges",
        node_type="problem_analysis",
        community_id=1,
        community_name="Problem Statement & Literature Survey",
        summary="Detailed problem statement: coarse NWP models, rapid convective storms, and data silos.",
        details=r"""# Problem Statement & Research Motivation

## 1. Coarse Spatial & Temporal Resolution in Standard NWP
- Global Numerical Weather Prediction (NWP) models (e.g., GFS at ~25 km, ECMWF IFS at ~9 km) update only every 6 to 12 hours.
- In coastal Tamil Nadu and Puducherry, intense rain cells during the Northeast Monsoon (NEM) can form, intensify, and dump >50 mm of rain within 30 to 90 minutes over a small radius of 3 to 10 km.
- Standard NWP completely misses these micro-scale convective flash floods.

## 2. High Risk of Urban Inundation and Disaster Vulnerability
- Low-lying coastal cities (Puducherry, Chennai, Cuddalore) experience severe waterlogging that impacts transit, power supply, and livelihoods.
- Authorities and citizens lack access to hyperlocal 0–2h and 0–3h quantitative precipitation nowcasts (QPF).

## 3. Data Fragmentation Across Meteorological Silos
- Existing weather platforms are fragmented:
  - **IMD Mausam**: High-quality official data, but limited automated public APIs and sparse station coverage in semi-urban belts.
  - **Personal Weather Stations (PWS) (Ambient Weather, Weather Underground)**: Dense community IoT stations measuring hyper-local temperature, pressure, and rain, but lacking predictive AI nowcasting.
  - **Global NWP Portals (Windy, RainViewer)**: High-level visual maps without localized ground-truth calibration or deep learning nowcast models.

## 4. The Research Objective
Develop a low-cost, multi-source weather data fusion platform that combines dense ground IoT sensors, numerical forecasts, and deep learning attention models for real-time hyperlocal precipitation nowcasting.""",
        file_path="Project brief.md"
    )

    add_node(
        node_id="literature_survey_benchmark",
        label="Literature Survey Master Table (16 Papers)",
        node_type="literature_review",
        community_id=1,
        community_name="Problem Statement & Literature Survey",
        summary="Exhaustive literature survey table synthesizing all 16 papers from Chapter 2 and the project library.",
        details=r"""# Literature Survey: Complete 16 Papers Matrix

| S.No | Paper Title | Authors | Year | Venue | Key Contribution | Disadvantage / Research Gap Addressed |
|---|---|---|---|---|---|---|
| 1 | **ConvLSTM Network: A Machine Learning Approach for Precipitation Nowcasting** | Xingjian Shi et al. | 2015 | NeurIPS / arXiv | Replaces FC-LSTM with convolutional gates in input-to-state and state-to-state transitions. | Blurs severely at >60 min due to MSE; ignores ground IoT sensor readings. |
| 2 | **Deep Learning for Precipitation Nowcasting: A Benchmark and a New Model** | Xingjian Shi et al. | 2017 | NeurIPS | Introduces Trajectory GRU (TrajGRU) to learn location-variant dynamic recurrent connections. | High computational complexity; radar-centric without IoT fusion. |
| 3 | **Precipitation Nowcasting: Leveraging Bidirectional LSTM and 1D CNN** | Patel, Patel & Ghosh | 2018 | arXiv | Combines 1D CNN feature extractors with BiLSTM for temporal atmospheric dependency. | Single-station focus; does not capture spatial relationships across sensor networks. |
| 4 | **LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module (BASE PAPER)** | Xiaoping Geng, Chen Zhang et al. | 2023 | Sensors (MDPI) | U-Net with Depthwise Separable Convolutions (DSC), Vertical Flow ConvLSTM, ECSA Attention, and TLoss. | Parameter cut by 41.86%, but ConvLSTM experiences memory decay at lead times >90 min. Authors explicitly proposed Transformer as future work. |
| 5 | **ConvLSTM Network-Based Rainfall Nowcasting with Combined Reflectance and Wind** | Wang et al. | 2022 | Atmosphere | Dual-input ConvLSTM using Doppler radar reflectance and retrieved horizontal wind fields. | Highly dependent on Doppler Weather Radar; lacks PWS ground calibration. |
| 6 | **Two-Stream Convolutional LSTM for Precipitation Nowcasting** | Recent studies | 2022 | Neural Computing & Appl. | Two parallel streams processing spatial radar intensity and velocity fields separately. | Large memory footprint; challenging to deploy on lightweight edge servers. |
| 7 | **A Data-Driven Approach for High Accurate Spatiotemporal Precipitation Estimation** | Recent studies | 2024 | Neural Computing & Appl. | GNN encoder-decoder with multimodal fusion modeling station spatial relationships. | Requires predefined graph topologies and struggles with dynamic station dropouts. |
| 8 | **Automated Predictive Analytics for Localized Rainfall** | Weather AI Team | 2022 | IEEE Access | Automated feature engineering on barometric pressure and humidity tendencies. | Relies solely on tabular tree ensembles without learning spatiotemporal motion. |
| 9 | **Skilful Precipitation Nowcasting Using Deep Generative Models of Radar (DGMR)** | Suman Ravuri et al. | 2021 | Nature (DeepMind) | Generative adversarial network with spatial and temporal discriminators producing sharp radar fields. | Extreme computational cost (TPU clusters); unsuitable for sparse IoT deployment. |
| 10 | **ECMWF Short-Term Numerical Weather Prediction Downscaling** | European Centre | 2023 | QJRMS | Statistical and machine learning downscaling of ECMWF global GRIB2 forecasts to local stations. | 6-hour forecast latency makes it incapable of 0–60 minute convective nowcasting. |
| 11 | **A Structured Graph Neural Network for Improving NWP (GIPMN)** | Climate ML Group | 2024 | AI for Earth | Combines numerical physical equations with GNN spatial station graphs. | Heavy alignment complexity between gridded NWP and irregular station points. |
| 12 | **Data-Driven Global Precipitation Estimation from Satellite Imagery** | Remote Sensing Lab | 2021 | IEEE TGRS | Infrared and microwave geostationary satellite imagery to estimate surface precipitation. | Coarse spatial resolution (4–10 km); satellite parallax errors in coastal zones. |
| 13 | **ConvCast: Convolutional Nowcasting over Radar Grids** | Radar Tech Group | 2023 | Weather & Forecasting | Multi-layer 3D convolutional nowcaster forecasting radar reflectivity cubes. | Misses surface thermodynamic parameters (dew point, relative humidity). |
| 14 | **Predicting Rainfall Using Machine Learning & Deep Learning Ensembles** | Applied ML Lab | 2023 | Springer | Benchmarked Random Forest, XGBoost, and LightGBM against basic LSTM on tabular data. | Lack of spatial awareness and unable to generate 2D forecast maps. |
| 15 | **Short-Term Precipitation Forecasting with Attention U-Net** | Vision ML Group | 2022 | Remote Sensing | Standard spatial attention gates on U-Net skip connections. | Collapses channels using global pooling, losing channel-specific moisture signals. |
| 16 | **Enhancing Weather Radar Nowcasting with Multi-Task Loss Functions** | Meteorological AI | 2024 | J. Hydrometeorology | Combines balanced MSE with focal cross-entropy to handle heavy rainfall class imbalance. | Solves loss imbalance but retains blurry recurrent architectures. |""",
        file_path="Bharath B - FYP Report.docx"
    )

    add_node(
        node_id="base_paper_deep_dive",
        label="Base Paper Deep Dive: LSTMAtU-Net (Sensors 2023)",
        node_type="scientific_foundation",
        community_id=1,
        community_name="Problem Statement & Literature Survey",
        summary="Exhaustive analysis of the base paper LSTMAtU-Net: DSC, ECSA module, ConvLSTM-VF, and TLoss.",
        details=r"""# Base Paper: LSTMAtU-Net (Sensors 2023)
- **Title**: LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module
- **Authors**: Xiaoping Geng, Chen Zhang, Yujie Wang, et al.
- **Journal**: *Sensors* 2023, 23(13), 5785. DOI: [10.3390/s23135785](https://doi.org/10.3390/s23135785).

## Four Foundational Innovations:
1. **Depthwise Separable Convolutions (DSC)**:
   - Decomposes standard 2D convolution into depthwise (per-channel spatial filtering) and pointwise (1x1 cross-channel linear combination).
   - Reduces parameter count from 32,024,420 (standard U-Net) to **18,619,421** (41.86% parameter reduction).
   - Dramatically lowers inference latency, enabling rapid nowcast cycles.

2. **Efficient Channel and Space Attention (ECSA) Module**:
   - Standard ECA modules use Global Average Pooling (GAP) which reduces the spatial dimensions to 1x1, obliterating crucial spatial rain cell boundaries.
   - ECSA replaces GAP with multi-scale **Adaptive Average Pooling (AAP)** of scale $R \times R$ ($R \in \{16, 8, 4, 2, 1\}$ matched to U-Net encoder levels), followed by 1D convolution ($k=3$) along the channel axis.
   - Retains multi-scale spatial topology while adaptively weighting key moisture and velocity channels.

3. **Vertical Flow ConvLSTM (ConvLSTM-VF)**:
   - Rotates the traditional temporal ConvLSTM 90° clockwise.
   - Memory $M^l$ and hidden representation $H^l$ flow **vertically** across network abstraction layers $l$, establishing rich hierarchical representations between multi-scale U-Net encoder-decoder stages.

4. **Multi-Objective Weighted Loss (TLoss)**:
   - Directly tackles extreme class imbalance (90%+ dry periods).
   - Combines Weighted MSE ($\text{WMSE}$) with multi-threshold soft Binary Cross-Entropy ($\text{BCE}_p$) at meteorological thresholds $p \in \{0.05, 0.5, 1.0\}\text{ mm}$.
   - Exponential weighting factor: $w(y) = e^{0.6y} - 0.8$, penalizing severe rainfall prediction misses heavily.""",
        file_path="ml-pipeline/src/lstmatu_net.py"
    )

    add_node(
        node_id="proposed_transatunet_novelty",
        label="Proposed Novel Extension: TransAtU-Net Architecture",
        node_type="scientific_novelty",
        community_id=1,
        community_name="Problem Statement & Literature Survey",
        summary="Novel contribution of this FYP: Fulfilling base paper's future research direction via Spatio-Temporal Transformers.",
        details=r"""# Proposed Novel Extension: TransAtU-Net Architecture

## Scientific Motivation (Direct Quote from Base Paper)
In Section 5 of Geng et al. (*Sensors 2023*), the authors explicitly state:
> *"Therefore, our future research will focus on the Transformer architecture and the weighted loss function to improve the precipitation nowcasting accuracy."*

Our Final Year Project directly answers and implements this research challenge.

## Core Architectural Enhancements in TransAtU-Net:
1. **Spatio-Temporal Multi-Head Self-Attention (ST-MHSA) Bottleneck**:
   - Replaces the sequential, recurrent ConvLSTM cell with full self-attention across flattened space and time tokens.
   - **Solves the Recurrent Blur Problem**: Standard recurrent cells (LSTM/GRU) suffer from vanishing gradients and error accumulation as lead time progresses to 90–120 minutes. Transformer attention provides direct $O(1)$ token interaction across all lead-time horizons.
   - Captures non-local meteorological interactions between convective cloud clusters across distant districts simultaneously.

2. **ECSA on Multi-Scale Skip Connections**:
   - Retains the ECSA module on U-Net skip connections to preserve localized gradient sharpness and rain contour boundaries.

3. **Multi-Lead Temporal Positional Encodings**:
   - Injects explicit sinusoidal temporal embeddings for forecast horizons (+15m, +30m, +45m, +60m, +90m, +120m).

4. **Enhanced Focal Weighted Loss**:
   - Extends TLoss by incorporating focal modulating factors $(1 - p_t)^\gamma$ to prevent overwhelming gradients from easy non-rain samples, while retaining severe rainfall threshold penalties.""",
        file_path="ml-pipeline/src/transformer_nowcast.py"
    )

    # =========================================================================
    # COMMUNITY 2: Mathematical Formulations & DL Theory
    # =========================================================================
    add_node(
        node_id="math_ecsa_formulation",
        label="Mathematical Formulation: ECSA Module",
        node_type="mathematical_formula",
        community_id=2,
        community_name="Mathematical Formulations & DL Theory",
        summary="Detailed equations and tensor dimensions for Efficient Channel and Space Attention.",
        details=r"""# Efficient Channel and Space Attention (ECSA) Formulation

## Governing Formula:
$$\tilde{X} = \sigma\left(\text{Conv1D}_{k=3}\left(\text{Mean}_{R \times R}\left(\text{AAP}(X, R)\right)\right)\right) \odot X$$

## Execution Steps:
1. **Adaptive Average Pooling (AAP)**:
   - Input: $X \in \mathbb{R}^{B \times C \times H \times W}$
   - Pooling to scale $R \times R$: $X_{\text{pooled}} = \text{AAP}(X, (R, R)) \in \mathbb{R}^{B \times C \times R \times R}$
   - Where $R \in \{16, 8, 4, 2, 1\}$ corresponds to each hierarchical level of the U-Net.
2. **Spatial Descriptor Compression**:
   - Average across the $R \times R$ grid:
   - $s_c = \frac{1}{R^2} \sum_{i=1}^R \sum_{j=1}^R X_{\text{pooled}}(c, i, j) \in \mathbb{R}^{B \times C}$
3. **1D Channel Convolution**:
   - Reshape to $\mathbb{R}^{B \times 1 \times C}$
   - Compute fast 1D convolution with kernel size $k=3$ (odd kernel preserving cross-channel local interaction without dimensionality reduction):
   - $\omega = \sigma\left(\text{Conv1D}_{k=3}(s)\right) \in \mathbb{R}^{B \times 1 \times C}$
4. **Channel-Spatial Calibration**:
   - Reshape $\omega$ to $\mathbb{R}^{B \times C \times 1 \times 1}$ and element-wise multiply with original feature map $X$:
   - $\tilde{X} = X \odot \omega$""",
        file_path="ml-pipeline/src/ecsa.py"
    )

    add_node(
        node_id="math_dsc_convolutions",
        label="Mathematical Formulation: Depthwise Separable Convolutions",
        node_type="mathematical_formula",
        community_id=2,
        community_name="Mathematical Formulations & DL Theory",
        summary="Mathematical comparison of standard 2D convolution vs Depthwise Separable Convolutions.",
        details=r"""# Depthwise Separable Convolutions (DSC)

## Parameter & FLOP Comparison:
Let $D_K \times D_K$ be kernel spatial size ($3 \times 3$), $D_F \times D_F$ be feature map dimensions, $M$ be input channels, and $N$ be output channels.

### Standard 2D Convolution:
- Computational cost: $D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$
- Number of parameters: $D_K^2 \cdot M \cdot N$

### Depthwise Separable Convolution:
1. **Depthwise Convolution** (Spatial filtering per channel):
   - Cost: $D_K \cdot D_K \cdot M \cdot D_F \cdot D_F$
   - Parameters: $D_K^2 \cdot M$
2. **Pointwise Convolution** (1x1 Linear channel projection):
   - Cost: $M \cdot N \cdot D_F \cdot D_F$
   - Parameters: $M \cdot N$

### Theoretical Reduction Ratio:
$$\text{Reduction} = \frac{D_K^2 \cdot M + M \cdot N}{D_K^2 \cdot M \cdot N} = \frac{1}{N} + \frac{1}{D_K^2} \approx \frac{1}{9} \approx 11.1\% \text{ of standard FLOPs}$$
In the full U-Net architecture, this translates to a **41.86% reduction in total parameters** (from 32,024,420 down to 18,619,421), enabling sub-20ms inference latency on modern GPUs.""",
        file_path="ml-pipeline/src/lstmatu_net.py"
    )

    add_node(
        node_id="math_loss_functions",
        label="Mathematical Formulation: Multi-Objective TLoss & Focal Loss",
        node_type="mathematical_formula",
        community_id=2,
        community_name="Mathematical Formulations & DL Theory",
        summary="Formulation of TLoss (WMSE + multi-threshold soft BCE) and the Enhanced Focal Weighted Loss.",
        details=r"""# Precipitation Loss Functions

## 1. Base Paper TLoss (Equation 5)
$$L_{\text{TLoss}} = \text{WMSE} + 0.5 \sum_{p \in \{0.05, 0.5, 1.0\}} \text{BCE}_p$$

### A. Weighted Mean-Squared Error (WMSE)
$$\text{WMSE} = \frac{1}{N} \sum_{i=1}^N \left(y_i - \hat{y}_i\right)^2 \cdot w(y_i)$$
Where the exponential sample weighting function is defined as:
$$w(y) = e^{0.6 \cdot y} - 0.8$$
- For dry conditions ($y = 0\text{ mm}$): $w(0) = e^0 - 0.8 = 0.2$ (low penalty).
- For moderate rain ($y = 2\text{ mm}$): $w(2) = e^{1.2} - 0.8 \approx 2.52$ (high penalty).
- For heavy rain ($y = 5\text{ mm}$): $w(5) = e^{3.0} - 0.8 \approx 19.29$ (massive penalty).

### B. Multi-Threshold Soft Binary Cross-Entropy (BCE_p)
To directly optimize the Critical Success Index (CSI) at meteorologically critical thresholds:
$$\hat{y}_{i, p} = \sigma\left(\hat{y}_i - p\right)$$
$$y'_{i, p} = \mathbb{I}(y_i \ge p)$$
$$\text{BCE}_p = -\frac{1}{N} \sum_{i=1}^N \left[ y'_{i, p} \log(\hat{y}_{i, p} + \epsilon) + (1 - y'_{i, p}) \log(1 - \hat{y}_{i, p} + \epsilon) \right]$$
Thresholds evaluated:
- $p_1 = 0.05\text{ mm}$ (rain occurrence boundary)
- $p_2 = 0.50\text{ mm}$ (light-to-moderate threshold)
- $p_3 = 1.00\text{ mm}$ (heavy downpour threshold)

## 2. Enhanced Focal Weighted Loss (Proposed)
$$L_{\text{Focal}} = \text{WMSE} + \sum_{p} \alpha_p \left(1 - \hat{y}_{i, p}\right)^\gamma \text{BCE}_p$$
Focuses backpropagation on hard convective storm transitions while dynamically suppressing gradient noise from clear-sky background pixels.""",
        file_path="ml-pipeline/src/loss.py"
    )

    add_node(
        node_id="math_meteorological_metrics",
        label="Meteorological Evaluation Metrics (CSI, POD, FAR, HSS)",
        node_type="mathematical_formula",
        community_id=2,
        community_name="Mathematical Formulations & DL Theory",
        summary="Standard contingency table evaluation metrics for Quantitative Precipitation Forecasting.",
        details=r"""# Meteorological Evaluation Metrics

Quantitative Precipitation Forecasting (QPF) cannot be evaluated using $R^2$ or standard accuracy due to extreme class imbalance. The World Meteorological Organization (WMO) and base paper specify:

## 1. Contingency Table Definitions
Given a rainfall threshold $\tau$ (e.g. $0.05, 0.2, 0.5, 1.0\text{ mm}$):
- **TP (Hits)**: Prediction $\ge \tau$ AND Observed $\ge \tau$
- **FP (False Alarms)**: Prediction $\ge \tau$ AND Observed $< \tau$
- **FN (Misses)**: Prediction $< \tau$ AND Observed $\ge \tau$
- **TN (Correct Negatives)**: Prediction $< \tau$ AND Observed $< \tau$

## 2. Key Formulae
- **Critical Success Index (CSI / Threat Score)**:
  $$\text{CSI} = \frac{\text{TP}}{\text{TP} + \text{FP} + \text{FN}}$$
  Measures the fraction of observed and predicted rain events that were correctly forecasted. Best: 1.0, Worst: 0.0.

- **Probability of Detection (POD / Hit Rate)**:
  $$\text{POD} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
  Measures what fraction of actual rainfall was successfully caught.

- **False Alarm Rate (FAR)**:
  $$\text{FAR} = \frac{\text{FP}}{\text{TP} + \text{FP}}$$
  Measures what fraction of rain alarms were false.

- **Heidke Skill Score (HSS)**:
  $$\text{HSS} = \frac{2(\text{TP} \cdot \text{TN} - \text{FP} \cdot \text{FN})}{(\text{TP} + \text{FN})(\text{FN} + \text{TN}) + (\text{TP} + \text{FP})(\text{FP} + \text{TN})}$$
  Measures accuracy relative to random chance. Range: $-\infty$ to 1.0 ($>0$ indicates skill).

- **Continuous Metrics**: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) in millimeters.""",
        file_path="ml-pipeline/src/metrics.py"
    )

    # =========================================================================
    # COMMUNITY 3: Implementation Lifecycle & Empirical Results (Chapter 6)
    # =========================================================================
    add_node(
        node_id="implementation_15_steps_lifecycle",
        label="15-Step End-to-End Implementation Methodology (Chapter 6.1)",
        node_type="implementation_methodology",
        community_id=3,
        community_name="Implementation Lifecycle & Results",
        summary="Complete 15-step engineering methodology documented in Chapter 6 of the project report.",
        details=r"""# 15-Step Implementation Methodology (Chapter 6.1)

1. **Step 1: Project Environment Setup**: Python 3.13, Node 20+, PyTorch 2.7, FastAPI, Next.js 16.
2. **Step 2: Backend Application Development**: Asynchronous FastAPI core with Uvicorn ASGI server.
3. **Step 3: Integration of Weather Data Sources**: Connecting IMD AWS, Ambient PWS, and Open-Meteo.
4. **Step 4: Automated Data Acquisition**: APScheduler background runner polling at 60s intervals.
5. **Step 5: Data Storage Layer**: SQLAlchemy Async ORM with aiosqlite weather.db.
6. **Step 6: Data Cleaning & Validation**: Handling missing sensor values, out-of-range sensor spikes.
7. **Step 7: Timestamp Alignment & Fusion**: Rounding observations to nearest 10-minute intervals and merging.
8. **Step 8: Feature Engineering**: Barometric drop rates ($\Delta P_{1h}, \Delta P_{3h}$), humidity gradients, dew point spread.
9. **Step 9: AI/ML Model Development**: PyTorch neural network construction (DSC, ECSA, ST-MHSA).
10. **Step 10: Rainfall Nowcasting Engine**: Multi-horizon (+15m to +120m) inference service.
11. **Step 11: ECMWF NWP Data Processing**: Parsing GRIB2 files with xarray and cfgrib for 1–10 day context.
12. **Step 12: REST API Development**: Exposing 13 endpoints with Pydantic serialization.
13. **Step 13: Web Application Development**: Responsive dark-mode dashboard in Next.js 16 with Recharts.
14. **Step 14: Frontend-Backend Integration**: Asynchronous API client fetching telemetry and forecasts.
15. **Step 15: System Testing & Performance Verification**: End-to-end load testing, deduplication verification, API latency benchmarking.""",
        file_path="Bharath B - FYP Report.docx"
    )

    add_node(
        node_id="empirical_evaluation_results",
        label="Phase 1 Empirical Results & Performance Matrix (Table 6.1 & 6.2)",
        node_type="empirical_results",
        community_id=3,
        community_name="Implementation Lifecycle & Results",
        summary="Empirical evaluation results: 43-day continuous data collection, volume by source, and API latency benchmarks.",
        details=r"""# Phase 1 Empirical Results & Performance Matrix

## 1. 43-Day Continuous Data Acquisition Campaign:
- **Evaluation Period**: 12 August 2026 to 24 September 2026 (43 continuous days).
- **Ingestion Frequency**: 60 seconds (APScheduler).
- **Data Volume by Source (Table 6.1)**:
  - **Open-Meteo Adapter**: 1,780 readings across 10 virtual grid points in Tamil Nadu/Puducherry.
  - **Ambient / PWS Adapter**: 1,334 real physical readings across 6 Personal Weather Stations in Puducherry/Auroville.
  - **Total Real Ingested Telemetry**: > 3,114 verified readings during evaluation campaign.

## 2. API Endpoint Latency Benchmarks (Table 6.2):
| API Endpoint | HTTP Method | Functionality | Measured Avg Latency |
|---|---|---|---|
| `/api/overview` | `GET` | Dashboard system-wide statistics | **18.4 ms** |
| `/api/stations` | `GET` | All active stations with latest reading | **34.7 ms** |
| `/api/readings/latest` | `GET` | Latest single reading per station | **27.2 ms** |
| `/api/stations/{id}/readings` | `GET` | 24-hour time-series historical curve | **~38–45 ms** |
| `/api/nowcast/latest` | `GET` | Latest nowcast predictions | **< 5 ms** |

## 3. Physical Telemetry Verification (Figure 6.3):
- 48-hour continuous telemetry plot on **Sarvamangalam PWS (IAUROV10, Auroville)** verified physical diurnal cycles:
  - Mid-afternoon temperature peak corresponding cleanly to relative humidity troughs.
  - Barometric pressure drops ($> 1.2\text{ hPa/hr}$) reliably preceded rain peaks, confirming high predictive utility for Phase 2 DL models.""",
        file_path="Bharath B - FYP Report.docx"
    )

    # =========================================================================
    # COMMUNITY 4: Backend System Architecture & Implementation
    # =========================================================================
    add_node(
        node_id="backend_main_service",
        label="FastAPI Backend Main Service (main.py)",
        node_type="backend_service",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="Application entry point, lifespan management, APScheduler initialization, and root landing page.",
        details=r"""# FastAPI Backend Main Service (`backend/main.py`)

## Core Responsibilities:
1. **Application Lifespan Context Manager**:
   - `create_tables()`: Automatically generates SQLite/Postgres tables on startup.
   - `backfill_history()`: Performs asynchronous 24–48h historical data backfill on startup so graphs immediately render continuous curves.
   - `run_ingestion()`: Executes immediate live telemetry sync.
   - Schedules high-frequency periodic ingestion job via `AsyncIOScheduler` every 30 to 60 seconds.
2. **CORS Middleware**: Fully configured for cross-origin requests from the Next.js frontend (`localhost:3000`).
3. **Service Landing Root Endpoint (`GET /`)**: Custom dark-themed HTML landing page displaying system status, server port (8000), and links to `/docs` and the web frontend.
4. **Health Check Endpoint (`GET /health`)**: JSON liveness endpoint for Docker container probes.""",
        file_path="backend/main.py"
    )

    add_node(
        node_id="backend_config_service",
        label="Configuration & Environment Management (config.py)",
        node_type="backend_config",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="Pydantic Settings loading environment variables with production fallbacks.",
        details=r"""# Configuration Management (`backend/config.py`)

Manages typed configuration using `pydantic-settings`:
- `DATABASE_URL`: Defaults to `sqlite+aiosqlite:///./weather.db` for local dev; easily switched to PostgreSQL for production.
- `INGESTION_INTERVAL_SECONDS`: Periodic scheduler interval (default: 60s, configurable down to 30s).
- `OPEN_METEO_BASE_URL`: Base URL for Open-Meteo REST queries (`https://api.open-meteo.com/v1/forecast`).
- `AMBIENT_API_KEY` & `AMBIENT_APP_KEY`: Credentials for querying Ambient Weather Network / Weather Underground PWS.
- `IMD_API_TOKEN`: India Meteorological Department API token (for future expansion).
- `ENABLE_NOWCAST_SYNTHESIS`: Flag controlling on-the-fly deep learning synthetic fallback predictions.""",
        file_path="backend/config.py"
    )

    add_node(
        node_id="backend_database_engine",
        label="Asynchronous Database Engine (database.py)",
        node_type="backend_database",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="SQLAlchemy 2.0 Async engine with aiosqlite and async sessionmaker.",
        details=r"""# Asynchronous Database Engine (`backend/database.py`)

## Technical Architecture:
- Built with SQLAlchemy 2.0 asynchronous execution pattern.
- Uses `create_async_engine()` paired with `async_sessionmaker(expire_on_commit=False)`.
- Implements `get_db()` async generator dependency injected into FastAPI routers:
  ```python
  async def get_db() -> AsyncGenerator[AsyncSession, None]:
      async with AsyncSessionLocal() as session:
          yield session
  ```
- `create_tables()` initializes all ORM declarative tables asynchronously on startup.""",
        file_path="backend/database.py"
    )

    add_node(
        node_id="backend_orm_models",
        label="SQLAlchemy ORM Data Models (models.py)",
        node_type="database_models",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="Relational ORM models: Station, WeatherReading, and NowcastPrediction.",
        details=r"""# SQLAlchemy ORM Models (`backend/models.py`)

1. **`Station` Table**:
   - `id`: Integer Primary Key
   - `station_id`: String (Unique, Indexed)
   - `name`: String (Station name)
   - `source`: String (`'ambient-pws'`, `'open-meteo'`, `'imd'`)
   - `lat`, `lon`: Floats (Geographic coordinates)
   - `city`, `state`: Strings (Territory / District)
   - `is_active`: Integer (Status flag)

2. **`WeatherReading` Table**:
   - `id`: Integer Primary Key
   - `station_id`: String (Foreign Key, Indexed)
   - `timestamp`: DateTime (UTC, Indexed)
   - `temp_c`, `humidity_pct`, `pressure_hpa`, `rainfall_mm`, `wind_speed_kmh`, `wind_direction_deg`: Floats
   - `raw_data`: Text (Raw JSON payload)

3. **`NowcastPrediction` Table**:
   - `id`: Integer Primary Key
   - `station_id`: String (Indexed)
   - `generated_at`: DateTime (UTC)
   - `valid_for`: DateTime (UTC)
   - `rain_probability`: Float (0.0 to 1.0)
   - `rain_intensity_mm`: Float
   - `model_version`: String (`'transatunet-v1.0'`, `'lstmatunet-v1.0'`)""",
        file_path="backend/models.py"
    )

    add_node(
        node_id="backend_schemas_validation",
        label="Pydantic Schemas & API Serializers (schemas.py)",
        node_type="backend_schemas",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="Strict request/response Pydantic schemas validating API payloads.",
        details=r"""# Pydantic Schemas (`backend/schemas.py`)

- `WeatherReadingBase` & `WeatherReadingOut`: Serializes temperature, humidity, pressure, rainfall, timestamps.
- `StationBase` & `StationOut`: Encapsulates station metadata and embeds its latest `WeatherReadingOut`.
- `NowcastPredictionOut`: Formats model lead times, probability, and estimated precipitation.
- `DashboardOverview`: Encapsulates total active stations, reading counts, and network-wide atmospheric averages.""",
        file_path="backend/schemas.py"
    )

    add_node(
        node_id="backend_ingestion_engine",
        label="Scheduled Ingestion & Deduplication Service (ingestion.py)",
        node_type="backend_ingestion",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="Asynchronous scheduled ingestion engine with deduplication and startup historical backfill.",
        details=r"""# Scheduled Ingestion Engine (`backend/ingestion.py`)

## Core Functions:
1. `run_ingestion()`:
   - Queries all registered active adapters (`AmbientWeatherAdapter`, `OpenMeteoAdapter`).
   - Gathers readings concurrently via `asyncio.gather()`.
   - Checks `_reading_exists(station_id, timestamp)` before each insert to prevent duplicates.
   - Bulk commits new readings and updates station active timestamps.
2. `backfill_history(hours=48)`:
   - Triggered on server startup.
   - Fetches up to 48 hours of continuous hourly observations from adapters.
   - Ensures that when examiners open the frontend, 24h trend charts are immediately populated with continuous historical lines.""",
        file_path="backend/ingestion.py"
    )

    add_node(
        node_id="backend_weather_router",
        label="Weather API Router & Endpoints (routers/weather.py)",
        node_type="api_router",
        community_id=4,
        community_name="Backend Architecture & API Services",
        summary="FastAPI router exposing 13 REST endpoints for telemetry, AI nowcasts, and NWP blends.",
        details=r"""# Weather API Router (`backend/routers/weather.py`)

A 26KB core API router exposing:
- `GET /api/overview`: Dashboard summary statistics.
- `GET /api/stations`: All stations with latest reading attached.
- `GET /api/stations/{id}`: Single station details.
- `GET /api/stations/{id}/readings?hours=24`: Time-series readings for trend graphs.
- `GET /api/readings/latest`: Latest readings across all stations.
- `GET /api/nowcast/models`: Architectural specifications and benchmark CSI/POD scores of TransAtU-Net, LSTMAtU-Net, and ConvLSTM.
- `GET /api/nowcast/architecture-info`: Deep dive details into ECSA, DSC, and ST-MHSA.
- `GET /api/nowcast/predict`: Multi-horizon nowcast predictions (+15m, +30m, +45m, +60m, +90m, +120m).
- `GET /api/nowcast/latest`: Latest nowcast predictions.
- `GET /api/forecast/rainfall-blend`: 24-hour multi-model weighted rainfall accumulation across 20 districts based on ECMWF, GFS, ICON, NCUM, and AI.""",
        file_path="backend/routers/weather.py"
    )

    # =========================================================================
    # COMMUNITY 5: Data Adapters & Station Network Coverage
    # =========================================================================
    add_node(
        node_id="adapter_base_interface",
        label="WeatherAdapter Abstract Base Class (adapters/__init__.py)",
        node_type="adapter_pattern",
        community_id=5,
        community_name="Data Adapters & Weather Station Network",
        summary="Source-agnostic adapter interface ensuring vendor-neutral data acquisition.",
        details=r"""# Adapter Architecture (`backend/adapters/__init__.py`)

Defines the `WeatherAdapter` abstract class and `WeatherDataPoint` dataclass:
```python
class WeatherAdapter(ABC):
    @property
    @abstractmethod
    def source_name(self) -> str: ...
    @abstractmethod
    def is_available(self) -> bool: ...
    @abstractmethod
    async def fetch_readings(self) -> List[WeatherDataPoint]: ...
    @abstractmethod
    async def fetch_history(self, hours: int = 24) -> List[WeatherDataPoint]: ...
```
Decouples backend logic from vendor APIs, allowing transparent addition of radar grids, satellite feeds, or custom IoT microcontrollers.""",
        file_path="backend/adapters/__init__.py"
    )

    add_node(
        node_id="adapter_ambient_pws",
        label="Ambient Weather / PWS Adapter (adapters/ambient.py)",
        node_type="iot_adapter",
        community_id=5,
        community_name="Data Adapters & Weather Station Network",
        summary="Integration with 6 real live community Personal Weather Stations in Puducherry and Auroville.",
        details=r"""# Real PWS Network Adapter (`backend/adapters/ambient.py`)

Connects to 6 active community IoT stations around Puducherry and Auroville:
1. `IAUROV10` — Sarvamangalam PWS (Auroville / Irumbai): Farm microclimate, convective boundary layer. Lat: `11.98282`, Lon: `79.80799`.
2. `IAUROV11` — Auro Orchard PWS (Auroville / Orchard): Agro-forestry canopy, high soil moisture. Lat: `11.98770`, Lon: `79.79365`.
3. `IPONDI9` — Heritage Town PWS (Puducherry / White Town): Coastal urban heritage zone. Lat: `11.93600`, Lon: `79.83300`.
4. `IPONDI13` — Marie Oulgaret PWS (Puducherry / Oulgaret): High-density suburban zone. Lat: `11.92868`, Lon: `79.78241`.
5. `IAUROV6` — Bommayapalayam PWS (Auroville / Coastal): Coastal cliff overlooking Bay of Bengal. Lat: `11.99030`, Lon: `79.84118`.
6. `IAUROV12` — Auroville Central PWS (Matrimandir Area): Central plateau microclimate. Lat: `11.99250`, Lon: `79.80500`.""",
        file_path="backend/adapters/ambient.py"
    )

    add_node(
        node_id="adapter_openmeteo",
        label="Open-Meteo Regional Adapter (adapters/openmeteo.py)",
        node_type="api_adapter",
        community_id=5,
        community_name="Data Adapters & Weather Station Network",
        summary="Free high-reliability REST API adapter monitoring 10 Tamil Nadu & Puducherry urban hubs.",
        details=r"""# Open-Meteo Regional Adapter (`backend/adapters/openmeteo.py`)

Monitors 10 strategic geographic hubs across Tamil Nadu & Puducherry:
1. `OM-CHENNAI-01`: Chennai Central (Lat: 13.0827, Lon: 80.2707)
2. `OM-PONDY-01`: Puducherry Town (Lat: 11.9416, Lon: 79.8083)
3. `OM-MADURAI-01`: Madurai Central (Lat: 9.9252, Lon: 78.1198)
4. `OM-COIMBAT-01`: Coimbatore City (Lat: 11.0168, Lon: 76.9558)
5. `OM-TIRUCHI-01`: Tiruchirappalli City (Lat: 10.7905, Lon: 78.7047)
6. `OM-SALEM-01`: Salem City (Lat: 11.6643, Lon: 78.1460)
7. `OM-VELLORE-01`: Vellore City (Lat: 12.9165, Lon: 79.1325)
8. `OM-TIRUNELV-01`: Tirunelveli City (Lat: 8.7139, Lon: 77.7567)
9. `OM-THOOTHU-01`: Thoothukudi Port (Lat: 8.7642, Lon: 78.1348)
10. `OM-CUDDALO-01`: Cuddalore Town (Lat: 11.7480, Lon: 79.7714)""",
        file_path="backend/adapters/openmeteo.py"
    )

    add_node(
        node_id="adapter_imd_aws",
        label="IMD AWS Adapter Stub (adapters/imd.py)",
        node_type="api_adapter",
        community_id=5,
        community_name="Data Adapters & Weather Station Network",
        summary="Government India Meteorological Department AWS adapter stub ready for official token integration.",
        details=r"""# IMD AWS Adapter Stub (`backend/adapters/imd.py`)

Provides clean interface adherence for official IMD Automatic Weather Station data feeds:
- Prepared with target endpoints for regional IMD radar composites and Chennai Meenambakkam AWS.
- Configured with graceful exception handling and informative status flags awaiting government API token activation.""",
        file_path="backend/adapters/imd.py"
    )

    # =========================================================================
    # COMMUNITY 6: ML Pipeline Code & Deep Learning Implementation
    # =========================================================================
    add_node(
        node_id="ml_pipeline_overview",
        label="Machine Learning Pipeline Architecture Overview",
        node_type="ml_overview",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="PyTorch-based ML pipeline implementing base paper LSTMAtU-Net, proposed TransAtU-Net, and inference services.",
        details=r"""# ML Pipeline Architecture (`ml-pipeline/src`)

The machine learning directory contains standalone PyTorch architectures, loss modules, and real-time inference services:
- `ecsa.py`: Efficient Channel and Space Attention module.
- `lstmatu_net.py`: Base paper LSTMAtU-Net with DSC and ConvLSTM-VF.
- `transformer_nowcast.py`: Novel TransAtU-Net with Spatio-Temporal Multi-Head Attention.
- `loss.py`: Base paper TLoss and Enhanced Focal Loss.
- `metrics.py`: CSI, POD, FAR, HSS, MAE, RMSE evaluation.
- `nowcast_service.py`: Real-time multi-horizon inference service.
- `feature_engineering.py`: Barometric tendency and humidity gradients.
- `verify_models.py`: Sanity checking tensor shapes and forward passes.""",
        file_path="ml-pipeline/src"
    )

    add_node(
        node_id="ml_ecsa_module_code",
        label="ECSA Module PyTorch Implementation (ecsa.py)",
        node_type="ml_code",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="PyTorch module for Efficient Channel and Space Attention with multi-scale Adaptive Average Pooling.",
        details=r"""# ECSA Module Implementation (`ml-pipeline/src/ecsa.py`)

```python
class ECSAModule(nn.Module):
    def __init__(self, channels: int, spatial_scale: int = 4, kernel_size: int = 3):
        super().__init__()
        self.spatial_scale = spatial_scale
        self.aap = nn.AdaptiveAvgPool2d((spatial_scale, spatial_scale))
        self.conv1d = nn.Conv1d(
            in_channels=1, out_channels=1,
            kernel_size=kernel_size,
            padding=(kernel_size - 1) // 2, bias=False
        )
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, c, h, w = x.shape
        pooled = self.aap(x)
        channel_desc = pooled.mean(dim=(-2, -1))
        ch_in = channel_desc.unsqueeze(1)
        ch_weight = self.sigmoid(self.conv1d(ch_in))
        scale = ch_weight.squeeze(1).unsqueeze(-1).unsqueeze(-1)
        return x * scale
```""",
        file_path="ml-pipeline/src/ecsa.py"
    )

    add_node(
        node_id="ml_lstmatu_net_code",
        label="LSTMAtU-Net PyTorch Implementation (lstmatu_net.py)",
        node_type="ml_code",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="Complete PyTorch implementation of the base paper LSTMAtU-Net with DSC, ConvLSTM-VF, and ECSA.",
        details=r"""# LSTMAtU-Net PyTorch Implementation (`ml-pipeline/src/lstmatu_net.py`)

Includes:
- `DepthwiseSeparableConv`: 3x3 depthwise convolution + 1x1 pointwise projection + BatchNorm + ReLU.
- `DoubleDSCBlock`: Stacked dual DSC layers.
- `VerticalConvLSTMCell`: ConvLSTM cell passing spatial-temporal memory $M$ and hidden state $H$ vertically across network layers.
- `LSTMAtUNet`: Complete 4-level U-Net encoder-decoder network integrating ECSA modules on all skip connections.""",
        file_path="ml-pipeline/src/lstmatu_net.py"
    )

    add_node(
        node_id="ml_transformer_code",
        label="TransAtU-Net Transformer Implementation (transformer_nowcast.py)",
        node_type="ml_code",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="Novel proposed TransAtU-Net with Spatio-Temporal Multi-Head Self-Attention bottleneck.",
        details=r"""# TransAtU-Net Implementation (`ml-pipeline/src/transformer_nowcast.py`)

Includes:
- `SpatioTemporalAttentionBlock`: Multi-Head Attention (8 heads, $D=256$) over flattened space-time tokens.
- `Multi-Lead Positional Encodings`: Sinusoidal temporal encodings for +15m to +120m forecast horizons.
- Direct $O(1)$ token interaction preventing recurrent blur and memory decay over long horizons.""",
        file_path="ml-pipeline/src/transformer_nowcast.py"
    )

    add_node(
        node_id="ml_loss_code",
        label="Multi-Objective Loss Functions (loss.py)",
        node_type="ml_code",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="PyTorch implementations of BasePaperTLoss (WMSE + soft BCE) and EnhancedTransformerLoss.",
        details=r"""# Loss Functions (`ml-pipeline/src/loss.py`)

- `BasePaperTLoss`: Equation 5 from Sensors 2023 combining Weighted MSE ($e^{0.6y} - 0.8$) and multi-threshold soft BCE ($p \in \{0.05, 0.5, 1.0\}\text{ mm}$).
- `EnhancedTransformerLoss`: Adds focal modulating factors and severe precipitation boundary weighting.""",
        file_path="ml-pipeline/src/loss.py"
    )

    add_node(
        node_id="ml_metrics_code",
        label="Meteorological Metrics Evaluator (metrics.py)",
        node_type="ml_code",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="Evaluates contingency tables and computes CSI, POD, FAR, HSS, MAE, and RMSE.",
        details=r"""# Meteorological Metrics Evaluator (`ml-pipeline/src/metrics.py`)

- `compute_contingency_table(y_pred, y_true, threshold)`: Computes TP, FP, FN, TN.
- `evaluate_precipitation_metrics()`: Calculates CSI, POD, FAR, HSS, MAE, and RMSE across customizable precipitation thresholds ($0.05, 0.2, 0.5, 1.0\text{ mm}$).""",
        file_path="ml-pipeline/src/metrics.py"
    )

    add_node(
        node_id="ml_nowcast_service",
        label="Inference Service: HyperlocalNowcaster (nowcast_service.py)",
        node_type="ml_service",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="Production inference wrapper generating multi-horizon predictions with atmospheric physics fallbacks.",
        details=r"""# HyperlocalNowcaster (`ml-pipeline/src/nowcast_service.py`)

- Manages model weights and inference execution for `transatunet`, `lstmatunet`, and `convlstm`.
- Generates 6 discrete forecast horizons: +15m, +30m, +45m, +60m, +90m, +120m.
- Implements atmospheric thermodynamics heuristics (barometric tendencies and humidity gradients) as a robust fallback if deep learning weights are uncalibrated.""",
        file_path="ml-pipeline/src/nowcast_service.py"
    )

    add_node(
        node_id="ml_feature_engineering_code",
        label="Feature Engineering Module (feature_engineering.py)",
        node_type="ml_features",
        community_id=6,
        community_name="Deep Learning Nowcasting Engine",
        summary="Computes pressure drop rate, humidity gradient, and dew-point depression.",
        details=r"""# Feature Engineering (`ml-pipeline/src/feature_engineering.py`)

Extracts thermodynamic predictors:
- $\Delta P_{1h} = P_t - P_{t-1h}$ (Barometric tendency)
- $\Delta RH_{1h} = RH_t - RH_{t-1h}$ (Moisture advection rate)
- $T - T_d$ (Dew point depression / air saturation deficit via Magnus-Tetens formula)""",
        file_path="ml-pipeline/src/feature_engineering.py"
    )

    # =========================================================================
    # COMMUNITY 7: Frontend Meteorological Dashboard (web-app/src)
    # =========================================================================
    add_node(
        node_id="frontend_root_layout",
        label="Next.js 16 Root Layout & Design Tokens (layout.tsx & globals.css)",
        node_type="frontend_core",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Next.js 16 App Router root layout, fonts, and ocean-teal meteorological design system.",
        details=r"""# Root Layout & Design System (`web-app/src/app/layout.tsx`)

- Enforces dark mode styling with Inter and JetBrains Mono typography.
- Global navigation bar linking Home, Dashboard, Forecast, and Blog.
- Bespoke meteorological CSS variables (`--deep-blue`, `--teal`, `--midnight`, `--surface`, `--accent-rain`).""",
        file_path="web-app/src/app/layout.tsx"
    )

    add_node(
        node_id="frontend_page_home",
        label="Platform Homepage (page.tsx)",
        node_type="frontend_page",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Interactive hero section with animated weather particles, live platform stats, and architecture cards.",
        details=r"""# Platform Homepage (`web-app/src/app/page.tsx`)

- Dynamic Hero section with radar-style pulse animations.
- Live telemetry counters (active stations, total readings, regional average temp/humidity).
- 3-tier architecture breakdown explaining Data Ingestion, Deep Learning Nowcasting, and NWP Blending.
- Direct navigation links to the Dashboard and AI Forecast center.""",
        file_path="web-app/src/app/page.tsx"
    )

    add_node(
        node_id="frontend_page_dashboard",
        label="Live Dashboard Operations Page (dashboard/page.tsx)",
        node_type="frontend_page",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Real-time operations center with live station card grid, search filters, and 24h interactive trend charts.",
        details=r"""# Dashboard Operations Page (`web-app/src/app/dashboard/page.tsx`)

- Real-time station card grid showing Puducherry PWS and Tamil Nadu urban stations.
- 30-second automated polling with live status pulse.
- District and city search filter.
- Interactive Recharts 24h trend chart with toggles for Temperature, Humidity, Rainfall, and Pressure.""",
        file_path="web-app/src/app/dashboard/page.tsx"
    )

    add_node(
        node_id="frontend_page_forecast",
        label="Deep Learning Forecast Page (forecast/page.tsx)",
        node_type="frontend_page",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Interactive AI nowcast interface: model switcher, 15m-120m lead time curves, and architecture visualizer.",
        details=r"""# AI Forecast Page (`web-app/src/app/forecast/page.tsx`)

A 43KB comprehensive deep learning interface with 3 tabs:
1. **Forecast Tab**: Model switcher (`TransAtU-Net` vs `LSTMAtU-Net`), station dropdown, multi-horizon (+15m to +120m) probability and intensity area chart, confidence rating gauge.
2. **Architecture Tab**: Interactive schematics detailing DSC, ECSA, ConvLSTM-VF, and ST-MHSA.
3. **Benchmarks Tab**: Comprehensive evaluation matrix comparing CSI, POD, FAR, and HSS across forecast lead times.""",
        file_path="web-app/src/app/forecast/page.tsx"
    )

    add_node(
        node_id="frontend_component_rainfall_map",
        label="ToggleRainfallMap Component (ToggleRainfallMap.tsx)",
        node_type="frontend_component",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Interactive ChennaiRains replica: 5-model weighted blend map across 20 Tamil Nadu & Puducherry districts.",
        details=r"""# ToggleRainfallMap (`web-app/src/components/ToggleRainfallMap.tsx`)

- 5-Model weight sliders: ECMWF (35%), GFS (25%), ICON (20%), NCUM (10%), AI (10%).
- 5-Day synoptic outlook selector tabs.
- Color-coded IMD rainfall scale (Light, Moderate, Heavy, Very Heavy, Extremely Heavy, Torrential).
- District inspector modal displaying individual model predictions for any selected district.""",
        file_path="web-app/src/components/ToggleRainfallMap.tsx"
    )

    add_node(
        node_id="frontend_component_trend_chart",
        label="TrendChart Component (TrendChart.tsx)",
        node_type="frontend_component",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Recharts-based time-series chart rendering 24-48h historical telemetry curves.",
        details=r"""# TrendChart Component (`web-app/src/components/TrendChart.tsx`)

- Smooth spline area curves with custom linear gradients.
- Metric toggles for Temperature (°C), Humidity (%), Rainfall (mm), and Pressure (hPa).
- Interactive tooltip with exact timestamps and formatted values.""",
        file_path="web-app/src/components/TrendChart.tsx"
    )

    add_node(
        node_id="frontend_component_station_card",
        label="StationCard Component (StationCard.tsx)",
        node_type="frontend_component",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Glassmorphism weather station card with animated icons, status badges, and source labels.",
        details=r"""# StationCard Component (`web-app/src/components/StationCard.tsx`)

- Glassmorphism backdrop-blur panel styling.
- Displays Temperature, Humidity, Pressure, Rain, Wind speed.
- Dynamic data source indicator badge (`Ambient PWS` vs `Open-Meteo`).
- Active selection highlight linking the card to the primary trend chart.""",
        file_path="web-app/src/components/StationCard.tsx"
    )

    add_node(
        node_id="frontend_lib_api_client",
        label="Typed API Client & Types (lib/api.ts & lib/types.ts)",
        node_type="frontend_lib",
        community_id=7,
        community_name="Frontend Meteorological Dashboard",
        summary="Type-safe TypeScript API client handling asynchronous backend communication.",
        details=r"""# API Client & Type Definitions (`web-app/src/lib/api.ts`)

- `fetchStations()`: Queries `/api/stations`.
- `fetchOverview()`: Queries `/api/overview`.
- `fetchReadings(stationId, hours)`: Queries `/api/stations/{id}/readings`.
- `fetchNowcastModels()`: Queries `/api/nowcast/models`.
- `fetchNowcastPredictions(modelType)`: Queries `/api/nowcast/predict`.
- `fetchRainfallBlend(day, weights)`: Queries `/api/forecast/rainfall-blend`.""",
        file_path="web-app/src/lib/api.ts"
    )

    # =========================================================================
    # COMMUNITY 8: Multi-Model NWP Blend Guidance (ChennaiRains Replica)
    # =========================================================================
    add_node(
        node_id="nwp_blend_algorithm",
        label="Multi-Model NWP Ensemble Blending Engine",
        node_type="nwp_blend",
        community_id=8,
        community_name="NWP Multi-Model Blend Guidance",
        summary="Mathematical ensemble blending ECMWF, GFS, ICON, NCUM, and AI nowcaster across 20 districts.",
        details=r"""# Multi-Model NWP Ensemble Blending Engine

## Objective:
Combines global NWP models with our AI nowcaster to generate calibrated 24-hour rainfall accumulation maps across 20 districts:
$$R_{\text{blend}}(d) = w_{\text{ecmwf}} R_{\text{ecmwf}}(d) + w_{\text{gfs}} R_{\text{gfs}}(d) + w_{\text{icon}} R_{\text{icon}}(d) + w_{\text{ncum}} R_{\text{ncum}}(d) + w_{\text{ai}} R_{\text{ai}}(d)$$
Subject to $\sum w_m = 1.0$.

## Regional District Coverage:
- North Coastal TN: Chennai, Tiruvallur, Chengalpattu.
- Central Coastal: Puducherry, Auroville, Cuddalore Port.
- Delta Zone: Nagapattinam, Thanjavur, Trichy.
- Inland & South TN: Kanchipuram, Villupuram, Madurai, Coimbatore, Salem, Vellore, Tirunelveli, Thoothukudi, Kanyakumari, Ramanathapuram, Nilgiris.""",
        file_path="backend/routers/weather.py"
    )

    # =========================================================================
    # COMMUNITY 9: PPT Presentation Decks (All Reviews)
    # =========================================================================
    add_node(
        node_id="ppt_slide_deck_outline",
        label="Complete PPT Presentation Structure (19 Slides)",
        node_type="presentation_deck",
        community_id=9,
        community_name="PPT Presentation & Review Decks",
        summary="Slide-by-slide guide from Review 1 & 2 presentations ready for PPT preparation and speaker notes.",
        details=r"""# Complete PPT Presentation Slide Structure

Use this exact structure for preparing project review slides:

- **Slide 1: Title Slide**:
  - Title: Multi-Source AI for Hyperlocal Rainfall Nowcasting.
  - Team: Ariyan M (23UCS015), Bharath B (23UCS025), Hemnnath G (23UCS066).
  - Guide: Dr. N. Danapaquiame, HOD/CSE, Sri Manakula Vinayagar Engineering College.
- **Slide 2: Abstract**:
  - Problem of coarse NWP models, flash downpours, need for 0-3h nowcasting, and multi-source fusion (IMD AWS + 6 PWS + ECMWF).
- **Slide 3: Problem Statement**:
  - Fragmented data sources, lack of high-resolution convective warning, urban flood vulnerability in coastal TN/Puducherry.
- **Slide 4: Existing Systems & Limitations**:
  - Comparison of IMD Mausam, Windy, PWS standalone networks, and radar nowcasting limitations.
- **Slide 5: Proposed System Overview**:
  - 3-Layer Solution: Layer 1 Observation (60s ingestion), Layer 2 Intelligence (AI Nowcasting), Layer 3 Presentation (Next.js Dashboard).
- **Slide 6: System Architecture Diagram**:
  - Data sources -> Adapters -> APScheduler -> SQLite/Postgres -> FastAPI REST API -> Next.js Frontend.
- **Slide 7: Implementation Module 1 — Data Acquisition & Storage**:
  - FastAPI backend at port 8000, 30s scheduler, 48h startup backfill, deduplication logic, SQLite database.
- **Slide 8: Implementation Module 2 — Feature Engineering**:
  - Pressure tendency ($\Delta P_{1h}$), humidity gradients, dew point spread ($T - T_d$), inter-station spatial vectors.
- **Slide 9: Implementation — Frontend Dashboard**:
  - Glassmorphism station cards, live 30s polling, Recharts 24h trend curves, dark ocean-teal palette.
- **Slide 10: Module 3 — AI/ML Nowcasting Engine (Phase 2 Roadmap)**:
  - Baseline Random Forest/XGBoost -> LSTMAtU-Net base paper -> Proposed TransAtU-Net.
- **Slide 11: Module 4 — NWP Processing & Interactive Map**:
  - Multi-model rainfall blend (ECMWF, GFS, ICON, NCUM, AI) across 20 districts.
- **Slide 12: Module 5 — Blog, Community & User Feedback**:
  - Weather discussions, verified community observations, admin moderation.
- **Slide 13: Progress Tracker & Deliverables Status**:
  - Phase 1 Completed: Backend, Adapters, Ingestion, Database, Feature Engineering, Frontend Dashboard.
  - Phase 2 Planned: Model training, full ECMWF GRIB2 ingestion, production containerization.
- **Slides 14 & 15: Literature Survey (Parts 1 & 2)**:
  - Detailed table: Shi et al. (ConvLSTM 2015, TrajGRU 2017), Ravuri et al. (DGMR 2021), Geng et al. (LSTMAtU-Net 2023).
- **Slide 16: Scope & Objectives**:
  - Regional focus on Puducherry & Tamil Nadu; 6 real PWS stations; 0–3h nowcasting horizon.
- **Slide 17: Technology Stack**:
  - FastAPI, PyTorch, Next.js 16, React 19, Tailwind CSS v4, SQLAlchemy, SQLite, Recharts.
- **Slide 18: Conclusion & Next Steps**:
  - Summary of Phase 1 deliverables and immediate Phase 2 training milestones.
- **Slide 19: Key References**:
  - Citations of Sensors 2023, NeurIPS, Nature, and WMO guidelines.""",
        file_path="Hyperlocal_Rainfall_Nowcasting_FYP_2nd_Review_Phase1.pptx"
    )

    # =========================================================================
    # COMMUNITY 10: Live Demo Walkthrough Guide & 20 Viva Voce Q&As
    # =========================================================================
    add_node(
        node_id="demo_walkthrough_guide",
        label="Step-by-Step Live Demo Execution Guide",
        node_type="demo_guide",
        community_id=10,
        community_name="Demo Walkthrough & Viva Voce Guide",
        summary="Precise terminal commands, browser URLs, and talking points for conducting an A+ viva demonstration.",
        details=r"""# Step-by-Step Live Project Demonstration

Follow these exact steps during your practical examination or project review:

## Step 1: Start Backend API Server
Open PowerShell Terminal 1:
```powershell
cd d:\FYP-1\backend
uvicorn main:app --reload --port 8000
```
- **What to point out in terminal**:
  1. `🌧️ Hyperlocal Rainfall Nowcasting — Backend starting...`
  2. `✅ Database tables ready`
  3. `⏳ Backfilling 24-48h historical time-series telemetry...` (Highlight that it backfills history on boot so graphs are never empty!)
  4. `⏰ High-frequency ingestion scheduled every 60 seconds`
- **Verify in browser**:
  - Open `http://localhost:8000/` (Show customized landing page with status badge).
  - Open `http://localhost:8000/docs` (Show interactive Swagger UI with all 13 REST endpoints).

## Step 2: Start Next.js Frontend
Open PowerShell Terminal 2:
```powershell
cd d:\FYP-1\web-app
npm run dev
```
- Open `http://localhost:3000` in Google Chrome.

## Step 3: Showcase Homepage (`http://localhost:3000`)
- **Talking Point**: "Here is our root landing page featuring our ocean-teal meteorological design system, dynamic active station count, and the 3-tier architecture breakdown."
- Click **"Launch Live Dashboard"**.

## Step 4: Showcase Real-Time Operations Dashboard (`http://localhost:3000/dashboard`)
- **Show Live Station Cards**:
  - Point to real Puducherry/Auroville PWS stations: *Heritage Town (White Town)*, *Sarvamangalam (Irumbai)*, *Bommayapalayam (Coastal)*.
  - Point to Tamil Nadu urban stations: *Chennai Central*, *Madurai*, *Coimbatore*.
  - Explain live parameters: Temp, Humidity, Pressure, Rain, Wind.
- **Demonstrate Interactive Trend Chart**:
  - Click on **Heritage Town PWS**.
  - Toggle between **Temperature**, **Humidity**, and **Rainfall** tabs.
  - Explain: "The chart renders continuous 24-hour historical curves retrieved directly from our async SQLite database."
- **Show Live Polling**:
  - Point to the pulse badge showing 30s auto-refresh, and click the manual refresh icon.

## Step 5: Showcase Deep Learning Nowcasting (`http://localhost:3000/forecast`)
- Navigate to `/forecast`.
- **Demonstrate Model Switching**:
  - Select **TransAtU-Net (Proposed Transformer + ECSA)**.
  - Show the multi-horizon probability curve (+15m to +120m).
  - Switch to **LSTMAtU-Net (Base Paper)** and explain the difference: "Notice how TransAtU-Net maintains sharp confidence over 90-120 minutes because the Transformer self-attention avoids the recursive memory decay of ConvLSTM."
- Click **Architecture Tab**:
  - Show interactive modals for ECSA, DSC, and TLoss.
- Click **Benchmarks Tab**:
  - Show the CSI, POD, FAR comparison table.

## Step 6: Showcase Multi-Model Rainfall Blend (`http://localhost:3000/blog` or Map)
- Move the **ECMWF**, **GFS**, **ICON**, and **AI** sliders.
- Explain: "This replicates the ChennaiRains operational blend builder, allowing meteorologists to weight global NWP models with our local AI nowcaster across 20 districts."

## Step 7: Database Verification (Behind the Scenes)
Open PowerShell:
```powershell
python -c "import sqlite3; conn=sqlite3.connect('d:/FYP-1/backend/weather.db'); print('Total readings stored:', conn.execute('SELECT COUNT(*) FROM weather_readings').fetchone()[0])"
```
- Shows hundreds/thousands of real persistent records.""",
        file_path="d:/FYP-1/Project brief.md"
    )

    add_node(
        node_id="viva_qa_cheat_sheet",
        label="Top 20 Viva Voce / Review Q&A Cheat Sheet",
        node_type="viva_preparation",
        community_id=10,
        community_name="Demo Walkthrough & Viva Voce Guide",
        summary="Comprehensive answers to the top 20 questions examiners ask about rainfall nowcasting, DL architectures, and systems.",
        details=r"""# Top 20 Viva Voce & Review Q&A Cheat Sheet

### Q1: What is the core difference between Weather Forecasting and Precipitation Nowcasting?
**Answer**: Weather forecasting predicts synoptic conditions (large-scale fronts, temperature, pressure) over 12 hours to 10 days using Numerical Weather Prediction (NWP) models at 10–25 km resolution. Precipitation Nowcasting specifically predicts the exact location, timing, and intensity of rainfall over the **immediate 0 to 2 or 3 hours** at **hyperlocal resolution (1 to 5 km)**.

### Q2: Why is standard Mean Squared Error (MSE) ineffective for training rainfall nowcasting models?
**Answer**: Rainfall data suffers from **extreme class imbalance**; over 90% of timestamps in any given season have 0 mm of precipitation. If trained with standard MSE, a neural network minimizes loss by predicting near-zero or blurred mean values everywhere, completely failing to detect heavy localized downpours. We solve this by using the base paper's **TLoss**, which introduces an exponential weighting penalty ($e^{0.6y} - 0.8$) and soft Binary Cross-Entropy at meteorological thresholds (0.05, 0.5, 1.0 mm).

### Q3: How do Depthwise Separable Convolutions (DSC) benefit this project?
**Answer**: Standard 2D convolution applies kernels across spatial and channel dimensions simultaneously, requiring $K \times K \times C_{\text{in}} \times C_{\text{out}}$ parameters. DSC splits this into depthwise (spatial filtering per channel, $K^2 C_{\text{in}}$) and pointwise ($1 \times 1$ linear projection, $C_{\text{in}} C_{\text{out}}$). In LSTMAtU-Net, this cuts parameters by **41.86%** (from 32M down to 18.6M) with virtually zero drop in accuracy, allowing rapid inference within 20 milliseconds.

### Q4: What is the Efficient Channel and Space Attention (ECSA) module?
**Answer**: Standard Efficient Channel Attention (ECA) uses Global Average Pooling (GAP) down to $1 \times 1$, which obliterates spatial rain cell boundaries. ECSA replaces GAP with **Adaptive Average Pooling (AAP)** to a multi-scale $R \times R$ grid ($R \in \{16, 8, 4, 2, 1\}$), followed by a 1D convolution ($k=3$) along channels. This preserves spatial structural features across U-Net skip connections while adaptively weighting channel dependencies.

### Q5: What is your novel contribution beyond the base paper?
**Answer**: The base paper (*Sensors 2023*) explicitly stated in its conclusion that future work must explore the **Transformer architecture and weighted loss**. We fulfilled this by designing **TransAtU-Net**, which replaces the sequential ConvLSTM bottleneck with **Spatio-Temporal Multi-Head Self-Attention (ST-MHSA)**. This eliminates recurrent memory decay and blur over 90–120 minute horizons. Furthermore, we built a complete end-to-end full-stack platform integrating real PWS stations in Puducherry and multi-model NWP blending.

### Q6: How do you handle missing or delayed data from community PWS stations?
**Answer**: In our adapter layer, we employ non-blocking asynchronous HTTP timeouts. If a station misses an ingestion cycle, our deduplication and time-alignment logic flags it without halting the pipeline. For nowcasting inference, the model utilizes historical window buffers and spatial correlation with nearest neighboring stations to impute missing inputs.

### Q7: Why use SQLite in Phase 1 and PostgreSQL/TimescaleDB in Phase 2?
**Answer**: SQLite with `aiosqlite` is serverless, zero-configuration, and self-contained in a single portable file (`weather.db`), making it ideal for local testing, rapid feature engineering, and offline examiner demos. In Phase 2, because our database schema is built using SQLAlchemy Async ORM, switching to PostgreSQL with TimescaleDB hypertables requires only updating the `DATABASE_URL` environment variable without changing any application code.

### Q8: What is Vertical Flow ConvLSTM (ConvLSTM-VF)?
**Answer**: Standard ConvLSTM connects hidden states horizontally across temporal steps. ConvLSTM-VF rotates the recurrent cell 90 degrees clockwise so spatial-temporal memory $M^l$ and hidden state $H^l$ pass vertically across network abstraction layers $l$ of the U-Net. This allows low-level texture features from early encoder layers to dynamically enrich high-level semantic features before decoding.

### Q9: How do you evaluate Quantitative Precipitation Forecasting (QPF)?
**Answer**: We use the World Meteorological Organization standard contingency metrics: Critical Success Index (CSI), Probability of Detection (POD), False Alarm Rate (FAR), and Heidke Skill Score (HSS) evaluated at discrete rainfall thresholds ($0.05, 0.2, 0.5, 1.0\text{ mm}$), alongside MAE and RMSE.

### Q10: What is the Magnus-Tetens formula and why is it used?
**Answer**: It calculates the dew point temperature $T_d$ from dry-bulb temperature and relative humidity:
$T_d = \frac{b \cdot \alpha(T, RH)}{a - \alpha(T, RH)}$ with $a = 17.27, b = 237.7^\circ\text{C}$.
The difference $T - T_d$ (dew point spread) measures atmospheric saturation deficit; when it nears $0^\circ\text{C}$, precipitation is imminent.

### Q11: How does the startup backfill work?
**Answer**: On server startup, `backfill_history()` queries Open-Meteo and Ambient PWS for 24 to 48 hours of historical hourly telemetry, storing it in SQLite before the live scheduler begins. This guarantees that user graphs and trend charts render complete curves even immediately after booting.

### Q12: How is deduplication enforced?
**Answer**: The ingestion service queries `_reading_exists(station_id, timestamp)` before each insert, enforcing compound uniqueness and avoiding duplicate rows if the scheduler polls more frequently than the station reporting rate.

### Q13: What are the 5 models used in the ChennaiRains rainfall blend?
**Answer**: ECMWF (35%), GFS (25%), ICON (20%), NCUM (10%), and AI TransAtU-Net (10%).

### Q14: How does TransAtU-Net handle lead times?
**Answer**: It injects multi-lead temporal sinusoidal positional encodings directly into the token sequence, allowing the model to project cloud motion and intensity concurrently at +15m, +30m, +45m, +60m, +90m, and +120m.

### Q15: Why is Next.js 16 with App Router used?
**Answer**: Next.js 16 provides server-side rendering, streaming SSR, fast Turbopack compilation, and type-safe routing. It allows real-time interactive components (`use client`) to coexist with SEO-friendly pages.

### Q16: How many stations are actively monitored?
**Answer**: 16 stations: 6 real Personal Weather Stations in Puducherry and Auroville (Sarvamangalam, Auro Orchard, Heritage Town, Marie Oulgaret, Bommayapalayam, Auroville Central) and 10 regional Open-Meteo urban stations across Tamil Nadu.

### Q17: What is the average response time of the REST API?
**Answer**: Measured empirically in Phase 1: `/api/overview` responds in 18.4 ms, `/api/stations` in 34.7 ms, and historical time-series queries in 38–45 ms.

### Q18: What is the role of APScheduler?
**Answer**: It runs an in-process `AsyncIOScheduler` inside FastAPI, triggering `run_ingestion()` every 60 seconds without requiring external dependencies like Celery, RabbitMQ, or Redis.

### Q19: What is the difference between POD and CSI?
**Answer**: POD (Hit Rate) measures what fraction of actual rain was detected ($\text{TP}/(\text{TP}+\text{FN})$), but can be artificially inflated by always predicting rain. CSI ($\text{TP}/(\text{TP}+\text{FP}+\text{FN})$) penalizes both false alarms and misses, giving a true measure of nowcast skill.

### Q20: What is planned for Phase 2?
**Answer**:
1. Full model training on multi-season historical radar and station data.
2. Direct GRIB2 parsing from ECMWF Open Data using `cfgrib` and `xarray`.
3. User authentication via NextAuth.js and community weather discussion boards.
4. Containerized production deployment on cloud infrastructure with TimescaleDB.""",
        file_path="Bharath B - FYP Report.docx"
    )

    # =========================================================================
    # EDGES & RELATIONSHIPS
    # =========================================================================
    # Academic & Meta
    add_edge("project_academic_meta", "po_pso_curriculum_mapping", "aligns_with", "Satisfies ABET/NBA Criteria")
    add_edge("project_academic_meta", "system_specifications_hardware_software", "specifies_requirements", "Chapter 4 Requirements")
    add_edge("project_academic_meta", "problem_statement_and_motivation", "solves_problem", "Target Problem Definition")

    # Problem Statement to Literature
    add_edge("problem_statement_and_motivation", "literature_survey_benchmark", "analyzes_prior_art", "16 Survey Papers")
    add_edge("literature_survey_benchmark", "base_paper_deep_dive", "selects_foundation", "Paper #4: Sensors 2023")
    add_edge("base_paper_deep_dive", "proposed_transatunet_novelty", "proposes_extension", "Fulfills Future Research Direction")

    # Math to Deep Learning Models
    add_edge("base_paper_deep_dive", "math_ecsa_formulation", "defines", "Formulates ECSA Module")
    add_edge("base_paper_deep_dive", "math_dsc_convolutions", "defines", "Formulates DSC Convolutions")
    add_edge("base_paper_deep_dive", "math_loss_functions", "defines", "Formulates Base TLoss")
    add_edge("base_paper_deep_dive", "math_meteorological_metrics", "evaluates_with", "CSI, POD, FAR, HSS")
    add_edge("proposed_transatunet_novelty", "math_ecsa_formulation", "incorporates", "Applies ECSA on Skips")
    add_edge("proposed_transatunet_novelty", "math_loss_functions", "enhances", "Focal Weighted CSI Loss")

    # Implementation Lifecycle to Results
    add_edge("implementation_15_steps_lifecycle", "empirical_evaluation_results", "produces_results", "43-Day Validation Results")
    add_edge("implementation_15_steps_lifecycle", "backend_main_service", "implements_steps", "Steps 1-5: Backend & DB")
    add_edge("implementation_15_steps_lifecycle", "ml_pipeline_overview", "implements_steps", "Steps 8-10: ML Nowcasting")
    add_edge("implementation_15_steps_lifecycle", "frontend_page_dashboard", "implements_steps", "Steps 13-14: Dashboard UI")

    # Code Implementation Links (ML Pipeline)
    add_edge("ml_pipeline_overview", "ml_ecsa_module_code", "contains", "ecsa.py")
    add_edge("ml_pipeline_overview", "ml_lstmatu_net_code", "contains", "lstmatu_net.py")
    add_edge("ml_pipeline_overview", "ml_transformer_code", "contains", "transformer_nowcast.py")
    add_edge("ml_pipeline_overview", "ml_loss_code", "contains", "loss.py")
    add_edge("ml_pipeline_overview", "ml_metrics_code", "contains", "metrics.py")
    add_edge("ml_pipeline_overview", "ml_nowcast_service", "contains", "nowcast_service.py")
    add_edge("ml_pipeline_overview", "ml_feature_engineering_code", "contains", "feature_engineering.py")

    add_edge("ml_lstmatu_net_code", "ml_ecsa_module_code", "imports", "Uses ECSAModule in Skips")
    add_edge("ml_transformer_code", "ml_ecsa_module_code", "imports", "Uses ECSAModule in Skips")
    add_edge("ml_nowcast_service", "ml_transformer_code", "runs_inference_on", "TransAtU-Net Inference")
    add_edge("ml_nowcast_service", "ml_lstmatu_net_code", "runs_inference_on", "LSTMAtU-Net Inference")

    # Backend Architecture Links
    add_edge("backend_main_service", "backend_config_service", "loads_config", "Reads Settings")
    add_edge("backend_main_service", "backend_database_engine", "initializes", "Runs create_tables()")
    add_edge("backend_main_service", "backend_ingestion_engine", "schedules", "Runs APScheduler (60s)")
    add_edge("backend_main_service", "backend_weather_router", "mounts_router", "Mounts /api Endpoints")
    add_edge("backend_database_engine", "backend_orm_models", "manages_tables", "Station, Reading, Nowcast")
    add_edge("backend_weather_router", "backend_schemas_validation", "validates_with", "Pydantic Schemas")
    add_edge("backend_ingestion_engine", "backend_orm_models", "persists_to", "Stores WeatherReadings")
    add_edge("backend_ingestion_engine", "adapter_base_interface", "calls_adapters", "Polls All Active Adapters")
    add_edge("adapter_base_interface", "adapter_ambient_pws", "implemented_by", "Ambient PWS Adapter")
    add_edge("adapter_base_interface", "adapter_openmeteo", "implemented_by", "Open-Meteo Adapter")
    add_edge("adapter_base_interface", "adapter_imd_aws", "implemented_by", "IMD AWS Adapter")
    add_edge("backend_weather_router", "ml_nowcast_service", "invokes", "Calls HyperlocalNowcaster")
    add_edge("backend_weather_router", "nwp_blend_algorithm", "executes", "Calculates Rainfall Blend")

    # Frontend Platform Links
    add_edge("frontend_root_layout", "frontend_page_home", "wraps", "Root Layout for Home")
    add_edge("frontend_root_layout", "frontend_page_dashboard", "wraps", "Root Layout for Dashboard")
    add_edge("frontend_root_layout", "frontend_page_forecast", "wraps", "Root Layout for Forecast")
    add_edge("frontend_page_dashboard", "frontend_component_station_card", "renders", "Station Cards Grid")
    add_edge("frontend_page_dashboard", "frontend_component_trend_chart", "renders", "24h Historical Telemetry Chart")
    add_edge("frontend_page_forecast", "ml_nowcast_service", "visualizes", "Multi-Horizon Nowcast Timeline")
    add_edge("frontend_page_dashboard", "frontend_lib_api_client", "calls", "api.ts")
    add_edge("frontend_page_forecast", "frontend_lib_api_client", "calls", "api.ts")
    add_edge("frontend_component_rainfall_map", "frontend_lib_api_client", "calls", "api.ts")
    add_edge("frontend_lib_api_client", "backend_weather_router", "queries_over_http", "HTTP REST API")

    # Presentation, Demo & Viva
    add_edge("ppt_slide_deck_outline", "project_academic_meta", "presents", "Slide 1 & 2: Team & Abstract")
    add_edge("ppt_slide_deck_outline", "problem_statement_and_motivation", "presents", "Slide 3 & 4: Problem Statement")
    add_edge("ppt_slide_deck_outline", "literature_survey_benchmark", "presents", "Slide 14 & 15: 16 Papers Table")
    add_edge("ppt_slide_deck_outline", "base_paper_deep_dive", "presents", "Slide 10 & 14: Base Paper Analysis")
    add_edge("ppt_slide_deck_outline", "proposed_transatunet_novelty", "presents", "Slide 10 & 18: Proposed TransAtU-Net")
    add_edge("ppt_slide_deck_outline", "implementation_15_steps_lifecycle", "presents", "Slide 7-9: Implementation Modules")
    add_edge("ppt_slide_deck_outline", "empirical_evaluation_results", "presents", "Slide 13: Progress & Results")
    add_edge("ppt_slide_deck_outline", "system_specifications_hardware_software", "presents", "Slide 17: Tech Stack & Specs")

    add_edge("demo_walkthrough_guide", "backend_main_service", "executes", "Step 1: Start Backend (Port 8000)")
    add_edge("demo_walkthrough_guide", "frontend_page_dashboard", "executes", "Step 3: Demo Dashboard & Trends")
    add_edge("demo_walkthrough_guide", "frontend_page_forecast", "executes", "Step 4: Demo DL Nowcast Switching")
    add_edge("demo_walkthrough_guide", "frontend_component_rainfall_map", "executes", "Step 5: Demo Blend Sliders")

    add_edge("viva_qa_cheat_sheet", "base_paper_deep_dive", "defends", "Explains DSC, ECSA, ConvLSTM-VF")
    add_edge("viva_qa_cheat_sheet", "proposed_transatunet_novelty", "defends", "Defends Novel Transformer Choice")
    add_edge("viva_qa_cheat_sheet", "math_loss_functions", "defends", "Defends TLoss vs Standard MSE")
    add_edge("viva_qa_cheat_sheet", "empirical_evaluation_results", "defends", "Defends 43-Day Ingestion & Latencies")

    graph_data["nodes"] = nodes
    graph_data["links"] = links
    return graph_data

if __name__ == "__main__":
    kg = build_exhaustive_knowledge_graph()
    
    out_root = Path("d:/FYP-1/graph.json")
    out_dir = Path("d:/FYP-1/graphify-out")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_graphify = out_dir / "graph.json"

    with open(out_root, "w", encoding="utf-8") as f:
        json.dump(kg, f, indent=2, ensure_ascii=False)
        
    with open(out_graphify, "w", encoding="utf-8") as f:
        json.dump(kg, f, indent=2, ensure_ascii=False)

    sys.stdout.write(f"Successfully generated EXHAUSTIVE knowledge graph with {len(kg['nodes'])} nodes and {len(kg['links'])} edges.\n")
    sys.stdout.write(f"Files written:\n  1. {out_root.resolve()}\n  2. {out_graphify.resolve()}\n")
