# Datasets and Training Methods for Embodied Intelligence and World Models: A Survey (2025–2026)

## 1. Introduction: The Data Bottleneck in Embodied AI

### 1.1 The Critical Role of Real-World Data in Scaling Embodied Intelligence

The field of embodied artificial intelligence has reached a critical inflection point in 2025–2026, where **the availability and quality of training data has emerged as the fundamental determinant of progress**. Unlike large language models that benefit from internet-scale text corpora, embodied AI systems require physically grounded, multimodal data that captures the intricate interplay between perception, action, and environmental dynamics. This fundamental difference has created what researchers and industry practitioners increasingly refer to as the **"data bottleneck"**—a constraint that limits the scalability and generalization of robotic systems far more severely than algorithmic or computational limitations .

The embodied intelligence market has experienced substantial growth, expanding from **USD 2.21 billion in 2024 to USD 2.52 billion in 2025**, with projections indicating continued growth at a compound annual growth rate of **15.53% to reach USD 7.03 billion by 2032** . This economic expansion reflects both the tremendous commercial potential and the pressing technical challenges that demand innovative solutions in data infrastructure. The integration of advanced neural architectures into physical systems has accelerated across applications including autonomous driving, adaptive manufacturing, logistics, and service robotics, yet all these domains share a common dependency on access to diverse, high-quality training data that captures the full complexity of real-world physical interaction .

The fundamental challenge lies in the **multimodal nature of embodied intelligence**, which requires simultaneous processing and learning from visual perception, linguistic instruction, tactile feedback, and proprioceptive action signals. Traditional approaches to data collection have proven inadequate for this task, creating demand for entirely new paradigms that can capture the rich, structured information inherent in human physical interaction with the environment. The convergence of embodied intelligence research with world model development has further intensified this data requirement, as world models demand not merely action demonstrations but comprehensive predictive understanding of environmental dynamics .

#### 1.1.1 Limitations of Internet-Sourced and Simulation Data

The limitations of conventional data sources for embodied AI have become increasingly apparent through extensive research and industrial practice. **Internet-sourced content**, while abundant, suffers from fundamental incompatibilities with embodied learning objectives. Videos and images collected from the internet typically lack the structured action information, tactile feedback, and precise temporal alignment that embodied systems require for learning physical skills. The distribution of internet content heavily skews toward visually interesting or socially shared activities, creating systematic gaps in coverage of mundane but practically essential manipulation tasks .

**Simulation-based data generation** has emerged as a partial solution, enabling rapid collection of large-scale interaction data in controlled virtual environments. However, **the sim-to-real gap**—the systematic discrepancy between simulated and real-world physics, perception, and dynamics—has proven remarkably persistent. While simulation data can support initial policy learning and architecture development, policies trained exclusively in simulation typically fail to transfer robustly to physical hardware without extensive domain randomization, adaptation techniques, or real-world fine-tuning . The computational cost of high-fidelity physics simulation, particularly for deformable objects, fluids, and complex contact dynamics, further limits the scalability of purely simulation-based approaches.

The industry has responded to these limitations through **hybrid approaches** that combine multiple data sources, with typical training pipelines employing mixtures of approximately **10% teleoperated real-world data and 90% simulation data** . However, even these hybrid approaches struggle to achieve the reliability and generalization required for commercial deployment, indicating that fundamental advances in data collection methodology are necessary rather than incremental improvements to existing approaches.

#### 1.1.2 The Emergence of Human-Centric Data Collection Paradigms

Recognition of conventional data source limitations has catalyzed the development of **human-centric data collection paradigms** that place human demonstrators at the center of the data generation process. These paradigms leverage the remarkable physical intelligence that humans possess, capturing natural, skilled behavior in authentic operational contexts rather than constructing artificial demonstration scenarios . The human-centric approach offers several distinctive advantages: it inherently captures physically realistic behavior that respects the constraints of real-world physics, it naturally includes the multimodal sensory information that humans use for skilled manipulation, and it can be deployed in diverse, unstructured environments that would be impractical to simulate with high fidelity.

The implementation of human-centric paradigms has been enabled by advances in **wearable sensing technology**, which now permits comprehensive data capture without constraining natural human movement or requiring specialized laboratory environments. First-person perspective recording through head-mounted or body-worn sensors captures the visual information that would be available to an embodied agent operating in the same context, while distributed tactile and proprioceptive sensors record the rich haptic information that skilled human manipulators rely upon . This technological convergence has made it feasible to collect large-scale, high-quality embodied datasets that were previously impossible to obtain.

The human-centric paradigm also addresses the critical challenge of **task diversity and environmental coverage**. By deploying data collection in real production and living scenarios—hotel laundry operations, supermarket assembly lines, logistics warehouses—rather than controlled laboratory settings, this approach captures the full complexity and variability of real-world tasks . The resulting datasets inherently include the rare events, edge cases, and environmental diversity that are essential for training robust, generalizable embodied policies but are systematically underrepresented in constructed demonstration datasets.

#### 1.1.3 The Convergence of Embodied Intelligence and World Models

The period 2025–2026 has witnessed **accelerating convergence between embodied intelligence research and world model development**, creating new requirements and opportunities for data infrastructure. World models—internal representations that enable agents to predict future states conditional on actions—have emerged as a critical component for sample-efficient learning, long-horizon planning, and safe exploration in embodied systems . This convergence has profound implications for data requirements: world models demand not merely action demonstrations but comprehensive predictive understanding of environmental dynamics, including the consequences of actions that may never be executed in demonstration data.

The integration of world models with embodied control has motivated development of datasets that support both imitation learning and predictive model learning simultaneously. The **Vision-Language-Tactile-Action (VLTA) multimodal structure** exemplifies this integration, providing the rich sensory grounding that enables world models to learn accurate forward dynamics while also supporting direct policy learning from expert demonstrations . World models trained on such comprehensive data can support model-based reinforcement learning, enabling agents to practice and refine skills through mental simulation before physical execution.

Predictions for 2026 suggest that **world models will achieve substantially extended prediction horizons**, with coherent video prediction reaching approximately **one hour for simple robotic environments**, representing a significant advance from the current state-of-the-art of 5–10 minutes . This capability extension will require corresponding advances in training data quality and diversity, as accurate long-horizon prediction demands comprehensive coverage of environmental dynamics across diverse situations and timescales.

## 2. Large-Scale Multimodal Datasets for Embodied Intelligence (2025–2026)

### 2.1 The World In Your Hands (WIYH) Dataset

#### 2.1.1 Dataset Overview and Release Timeline

##### 2.1.1.1 Developer: TARS Robotics (Founded February 5, 2025)

The **World In Your Hands (WIYH) dataset** represents a landmark achievement in embodied intelligence data infrastructure, developed by **TARS Robotics**, a Shanghai-based company founded on **February 5, 2025** . TARS Robotics emerged with substantial financial backing, securing a **$120 million Angel Round** from investors including Lanchi Ventures, followed by a **$122 million Angel+ Round**, reflecting strong investor confidence in the company's technical approach and market opportunity . This funding has enabled rapid development and deployment of the comprehensive data infrastructure required for large-scale human-centric data collection.

The company's founding mission centers on **building trustworthy super-embodied intelligent systems**, with data infrastructure recognized as the foundational enabler for this objective. Dr. Ding Wenchao, Chief Scientist of TARS, has articulated the strategic significance of the WIYH dataset as enabling "for the first time, large-scale cross-industry and cross-task collection of visual, language, tactile, and action data from real-world environments," establishing the foundation for scaling laws in future embodied foundation models . This positioning reflects a deliberate strategy to address the data bottleneck that has constrained the entire field, with potential benefits extending far beyond TARS's own product development.

The company's technical approach places it in competitive position relative to other major embodied AI initiatives. TARS estimates that its human-centric data engine paradigm provides approximately **six months of lead time** over comparable projects such as Tesla's Optimus program . This temporal advantage, if maintained through continued execution, could prove decisive in establishing data and model standards that shape the broader industry ecosystem.

##### 2.1.1.2 Open Access Schedule: December 2025

The WIYH dataset was announced for **open access release in December 2025**, with availability extended to research institutions and industry partners . This open access strategy represents a significant contribution to the research community, as high-quality embodied datasets have historically been closely held competitive assets. The decision to release the dataset openly suggests confidence in continued technical leadership through ongoing data collection and model development rather than static dataset advantage.

The timing of the open access release—approximately ten months after company founding—indicates rapid development and validation of the data collection infrastructure. This accelerated timeline has been enabled by the substantial financial resources deployed and by strategic focus on establishing operational data collection pipelines rather than extended research and development of collection methodologies. The December 2025 release positions the dataset to influence research directions and benchmark development throughout 2026.

##### 2.1.1.3 Core Innovation: First Large-Scale Real-World VLTA Multimodal Dataset

The WIYH dataset's defining characteristic is its status as **the world's first large-scale, real-world Vision-Language-Tactile-Action (VLTA) multimodal dataset** designed specifically for embodied intelligence applications . This four-modality integration represents a substantial advance over prior datasets that typically captured fewer modalities or operated in more constrained settings. The VLTA structure directly addresses the multimodal nature of physical intelligence, where skilled manipulation depends on integrated processing of visual scene understanding, linguistic task specification, tactile contact information, and proprioceptive action feedback.

The **real-world operational context** distinguishes WIYH from simulation-based datasets and from datasets collected in controlled laboratory environments. By capturing authentic human operational workflows across diverse sectors, WIYH provides the environmental diversity and realistic complexity that simulation struggles to replicate . This real-world grounding is particularly valuable for training systems intended for commercial deployment, where performance in authentic operational contexts is the ultimate success criterion.

#### 2.1.2 Data Scale and Composition

##### 2.1.2.1 Over 100,000 Real Human Operation Videos

The WIYH dataset comprises **over 100,000 real human operation videos**, representing one of the largest collections of authentic human physical interaction data ever assembled . This scale substantially exceeds prior real-world embodied datasets, which have typically numbered in the thousands or low tens of thousands of demonstrations. The large scale enables training of high-capacity foundation models that can capture the full diversity of human manipulation skills rather than being limited to narrow task-specific policies.

The video-centric structure preserves the **temporal dynamics of skilled manipulation**, capturing not merely static configurations but the continuous trajectories and force profiles that characterize expert performance. This temporal richness is essential for learning smooth, efficient action policies and for understanding the predictive dynamics that underlie skilled anticipation and error recovery. The scale of 100,000+ videos provides sufficient coverage to support learning of common manipulation patterns while including adequate examples of rare but important situations.

##### 2.1.2.2 Coverage: 40+ Task Types, 100+ Human Skills, 520+ Real Objects

The dataset demonstrates remarkable diversity in task coverage, encompassing **more than 40 distinct task types** that span the range of practical manipulation activities . This task diversity ensures that models trained on WIYH develop generalizable manipulation understanding rather than overfitting to narrow task definitions. The task types include both simple pick-and-place operations and complex multi-step procedures requiring extended reasoning and planning.

The skill coverage extends to **over 100 distinct human skills**, capturing the varied techniques that humans employ for effective physical interaction . This skill diversity is particularly valuable for cross-task transfer learning, as models can acquire generalizable manipulation primitives that compose to address novel tasks. The skill representation includes both coarse motor patterns and fine manipulative techniques, supporting development of policies with appropriate granularity for different task requirements.

Object coverage includes **more than 520 distinct real-world objects**, providing the object diversity necessary for learning generalizable object understanding and manipulation strategies . This extensive object set includes items with varied geometries, material properties, and functional affordances, enabling models to develop robust object representations that transfer to novel items. The real-world object collection contrasts with the limited object sets typical of simulation environments, where object diversity is constrained by modeling effort and computational resources.

| WIYH Dataset Attribute         | Specification                         |
| :----------------------------- | :------------------------------------ |
| **Total demonstration videos** | 100,000+                              |
| **Task types**                 | 40+                                   |
| **Human skills**               | 100+                                  |
| **Real-world objects**         | 520+                                  |
| **Sensor types**               | 13+                                   |
| **Core modalities**            | Vision-Language-Tactile-Action (VLTA) |
| **Collection environment**     | Real production/commercial settings   |
| **Release date**               | December 2025                         |

##### 2.1.2.3 Multimodal Modalities: Vision-Language-Tactile-Action (VLTA)

The **VLTA multimodal structure** represents a comprehensive approach to capturing the information streams that humans integrate for skilled manipulation. The **vision modality** captures egocentric visual observations from the human operator's perspective, providing the visual grounding that supports object recognition, pose estimation, and motion planning. The **language modality** captures natural language task descriptions and instructions, enabling development of instruction-following capabilities and supporting human-robot communication .

The **tactile modality** represents a distinctive and technically challenging component, capturing the rich haptic information that humans rely upon for contact detection, force control, and material property assessment. Tactile data has been historically underrepresented in embodied datasets due to the difficulty of comprehensive tactile sensing, but its inclusion in WIYH reflects recognition of its critical importance for skilled manipulation. Research in 2025 has demonstrated substantial improvements from tactile integration, with **tactile-VLA architectures showing 21.9% improvement over vision-only baselines on pick-and-place tasks and achieving 90% success on charger insertion versus 25-40% for vision-only approaches** .

The **action modality** captures the proprioceptive and kinematic information describing human body and hand movements, providing the demonstration trajectories that directly supervise policy learning. The integration of these four modalities in a single, temporally aligned dataset enables development of models that fuse multiple information sources for robust perception and control.

#### 2.1.3 Data Collection Methodology: Human-Centric Paradigm

##### 2.1.3.1 First-Person Wearable Device Framework (SenseHub)

The WIYH dataset collection employs the **SenseHub wearable device platform**, which enables comprehensive multimodal data capture from a first-person perspective . The SenseHub system integrates multiple sensor types in a wearable configuration that follows natural human movement without constraining operational capability. This wearable approach contrasts with stationary or environment-mounted sensing systems that capture third-person perspectives and may miss critical egocentric visual information.

The first-person perspective is particularly important for embodied learning, as it provides the visual information that would be available to a robot operating in the same context. This perspective alignment eliminates the need for viewpoint transformation that complicates learning from third-person demonstrations, and naturally includes the visual occlusion patterns and attentional focusing that characterize skilled human performance. The wearable configuration enables data collection in diverse, unstructured environments that would be impractical to instrument with fixed sensing infrastructure.

##### 2.1.3.2 Natural Integration into Real Production and Living Scenarios

A defining characteristic of the WIYH collection methodology is its **deployment in authentic operational contexts rather than constructed demonstration scenarios** . Data collection occurs in real production facilities, commercial establishments, and living spaces where humans are performing genuine work tasks rather than demonstrations for recording purposes. This natural integration ensures that collected data captures the authentic challenges and environmental conditions of real-world operation, including time pressure, environmental variability, and genuine task objectives.

The natural integration approach addresses several limitations of controlled demonstration collection. Demonstrators performing for recording may exhibit systematic differences from natural task execution, including exaggerated movements, simplified strategies, or reduced error rates that do not represent realistic performance distributions. By capturing natural workflow, WIYH includes the **error recovery strategies, adaptive responses, and efficiency optimizations** that characterize expert performance in authentic contexts.

##### 2.1.3.3 Cross-Sector Coverage: Hotel Laundry, Supermarket Assembly, Logistics Operations

The WIYH dataset achieves environmental diversity through **deliberate cross-sector deployment**, with active collection in **hotel laundry operations, supermarket assembly and stocking, and logistics warehouse operations** . This sector diversity ensures coverage of varied task types, object sets, and environmental constraints that would be impossible to capture in any single operational domain.

**Hotel laundry operations** involve handling of deformable textile objects, requiring skills in grasping, folding, and organizing soft materials that present distinctive manipulation challenges. The repetitive but variable nature of laundry processing provides extensive coverage of core manipulation primitives while including the instance variation necessary for robust learning. **Supermarket assembly and stocking tasks** involve interaction with rigid packaged goods, requiring precise placement and spatial organization skills relevant to warehouse and retail automation. **Logistics operations** encompass the material handling and transport activities that constitute a major application domain for industrial robotics, with requirements for efficiency, reliability, and safety in high-throughput environments.

#### 2.1.4 Automated Annotation Pipeline: TARS Datacore Engine

##### 2.1.4.1 Atomic Task Annotation

The **TARS Datacore Engine** provides comprehensive automated annotation that structures raw sensor data into semantically meaningful task representations . **Atomic task annotation** decomposes complex activities into constituent action elements, identifying the fundamental manipulation primitives that compose complete procedures. This decomposition enables analysis of task structure, supports learning of reusable skills, and facilitates transfer between related tasks that share common substructures.

The automated nature of atomic task annotation eliminates the manual labeling effort that would otherwise constrain dataset scale, while ensuring consistent annotation criteria across the full dataset. The annotation system identifies action boundaries, classifies action types, and extracts relevant parameters such as target objects, contact locations, and force requirements.

##### 2.1.4.2 Image Perception Annotation

**Image perception annotation** provides dense visual understanding of scene content, including object detection and segmentation, pose estimation, and spatial relationship identification . This visual annotation enables development of visual perception modules that can interpret novel scenes and support manipulation planning. The automated annotation pipeline leverages advances in computer vision to generate labels that would be prohibitively expensive to produce through manual annotation at dataset scale.

##### 2.1.4.3 Vision-Language Annotation

**Vision-language annotation** establishes correspondences between visual scene elements and linguistic descriptions, supporting development of grounded language understanding and instruction following capabilities . This annotation includes object naming, action description, and spatial relation expression that links natural language to visual perception. The vision-language alignment is critical for enabling human-robot communication and for leveraging linguistic knowledge to guide visual attention and manipulation planning.

##### 2.1.4.4 Full-Process Automation Without Manual Intervention

A critical enabling feature of the TARS Datacore Engine is its achievement of **full-process automation without requiring manual annotation intervention** . This automation is essential for dataset scalability, as manual annotation costs would otherwise limit practical dataset size regardless of collection capability. The automated pipeline processes raw sensor data through all annotation stages, producing structured, labeled datasets ready for model training.

### 2.2 OpenAI Robotics Lab Household Task Dataset

#### 2.2.1 Data Collection Infrastructure

##### 2.2.1.1 San Francisco Robotics Lab Established February 2025

**OpenAI established a dedicated robotics laboratory in San Francisco in February 2025**, marking a significant expansion of the company's physical AI research capabilities . This facility represents OpenAI's strategic commitment to embodied intelligence, extending the company's foundational work in large language models and generative AI into the physical domain. The San Francisco location provides access to technical talent and research ecosystem while enabling close coordination with OpenAI's core AI research teams.

##### 2.2.1.2 Scale: ~100 Contract Data Collectors Operating 24/7

The OpenAI robotics lab operates at substantial scale, employing **approximately 100 contract data collectors working in continuous 24/7 operations** . This staffing level represents significant ongoing investment in data collection infrastructure, with personnel costs alone likely exceeding several million dollars annually. The around-the-clock operation maximizes utilization of the physical facility and robotic hardware, amortizing fixed infrastructure costs across maximum data throughput.

##### 2.2.1.3 Hardware Platform: Franka Robotic Arms with 3D-Printed GELLO Controllers

The data collection hardware centers on **Franka Emika Panda robotic arms**, a widely adopted research platform known for its precision, safety features, and accessibility . A distinctive feature of the OpenAI setup is the use of **3D-printed GELLO (Generalized Low-Cost Teleoperation) controllers** for teleoperation . The GELLO design provides an ergonomic master interface that maps human hand movements to robot end-effector commands, enabling intuitive demonstration without requiring specialized robotics expertise. The 3D-printed construction minimizes hardware cost and enables rapid iteration on controller design.

#### 2.2.2 Task Domain and Data Characteristics

##### 2.2.2.1 Focus: Large-Scale Household Task Datasets

The OpenAI robotics lab focuses specifically on **household task data collection**, targeting the domestic environment that represents a major application domain for service robotics . This focus complements the industrial and commercial emphasis of the WIYH dataset, providing coverage of a distinct but equally important application domain.

##### 2.2.2.2 Representative Tasks: Laundry Folding, Toast Placement

Specific tasks under active data collection include **laundry folding and toast placement**, representing different categories of household manipulation challenges . Laundry folding involves deformable object manipulation, while toast placement represents simpler but practically important manipulation requiring precise positioning.

##### 2.2.2.3 Expansion: Second Lab Planned for Richmond, California

OpenAI has announced plans for **a second robotics laboratory in Richmond, California**, indicating successful initial operations and commitment to continued scaling of data collection infrastructure .

#### 2.2.3 Collection Methodology: Large-Scale Teleoperation

##### 2.2.3.1 Human-in-the-Loop Demonstration Recording

The OpenAI collection methodology centers on **human-in-the-loop teleoperation**, where human operators directly control robotic hardware to perform target tasks . This approach captures human physical intelligence through direct demonstration, with the robot recording the sensory observations and executed actions that constitute training data.

##### 2.2.3.2 Continuous Around-the-Clock Operation Model

The **24/7 continuous operation model** maximizes data collection throughput from the fixed hardware infrastructure . This operational intensity reflects the high cost of robotic hardware and facility infrastructure, which must be amortized through maximum utilization to achieve cost-effective data generation.

### 2.3 Comparative Analysis of 2025–2026 Embodied Datasets

| Comparison Dimension  | WIYH (TARS Robotics)                          | OpenAI Robotics Dataset                          |
| :-------------------- | :-------------------------------------------- | :----------------------------------------------- |
| **Developer**         | TARS Robotics (Shanghai, founded Feb 5, 2025) | OpenAI (San Francisco, lab established Feb 2025) |
| **Collection method** | Human-centric wearable (SenseHub)             | Teleoperation with GELLO controllers             |
| **Demonstrator**      | Human operators performing natural tasks      | Human operators controlling robot arms           |
| **Scale**             | 100,000+ videos                               | Not publicly specified                           |
| **Modalities**        | **VLTA: Vision-Language-Tactile-Action**      | Primarily Vision-Action                          |
| **Task domain**       | 40+ types: logistics, assembly, laundry       | Household: folding, placement                    |
| **Environment**       | Real industrial/commercial settings           | Laboratory household simulation                  |
| **Annotation**        | Fully automated (TARS Datacore)               | Not specified                                    |
| **Open access**       | December 2025                                 | Not announced                                    |

#### 2.3.1 Scale Comparison: WIYH vs. OpenAI Robotics Dataset

WIYH provides explicitly quantified scale metrics that demonstrate substantial coverage across tasks, skills, and objects, with the **100,000+ video count establishing a new benchmark** for real-world embodied datasets. The OpenAI robotics dataset scale has not been publicly specified, though the substantial operational infrastructure suggests significant collection volume.

#### 2.3.2 Methodology Contrast: Human-Centric Wearable vs. Teleoperation

The fundamental methodological contrast centers on the relationship between human demonstrator and data capture system. **WIYH's wearable approach** captures human natural performance without robotic mediation, preserving full dexterity and sensory capability but introducing an embodiment gap for robot policy training. **OpenAI's teleoperation approach** ensures physical feasibility on target hardware but may constrain demonstration quality through interface limitations.

#### 2.3.3 Domain Coverage: Industrial/Commercial vs. Household Environments

The domain coverage is largely complementary: **WIYH emphasizes industrial and commercial operational environments** while **OpenAI focuses on household tasks** . This complementarity reflects different market assumptions and application priorities.

#### 2.3.4 Multimodality: VLTA Integration vs. Vision-Action Focus

**WIYH's full VLTA multimodal structure** represents a superset of information compared to typical teleoperation datasets' vision-action focus. The **tactile modality** in WIYH captures haptic information largely absent from teleoperation-based collection, where force feedback to the operator may be limited or absent .

## 3. Training Methods for Embodied Foundation Models (2025–2026)

### 3.1 The AWE2.0 Model: Training on WIYH Dataset

#### 3.1.1 Model Architecture and Capabilities

##### 3.1.1.1 Spatial Reasoning Enhancement

The **AWE2.0 model**, developed by TARS Robotics and trained on the WIYH dataset, incorporates **enhanced spatial reasoning capabilities** that enable sophisticated understanding of three-dimensional scene structure and object relationships . This spatial reasoning extends beyond simple object detection to encompass functional affordance understanding, support surface identification, and geometric constraint reasoning that supports effective manipulation planning.

##### 3.1.1.2 World Model Integration

AWE2.0 integrates **world model capabilities** that enable predictive understanding of environmental dynamics and action consequences . This world model component supports mental simulation of proposed actions, enabling evaluation of action outcomes before physical execution. The integration of world modeling with policy learning represents the convergence trend identified in the research literature.

##### 3.1.1.3 Cross-Embodiment Transfer Learning

A distinctive capability of AWE2.0 is **cross-embodiment transfer learning**, enabling application of skills learned from human demonstration to diverse robotic hardware platforms . This transfer capability addresses the embodiment gap between human demonstrators and robot executors, leveraging shared physical principles that govern interaction regardless of specific hardware implementation.

#### 3.1.2 Training Methodology

##### 3.1.2.1 Pre-training on Large-Scale VLTA Multimodal Data

The AWE2.0 training methodology centers on **large-scale pre-training using the full WIYH VLTA multimodal dataset** . This pre-training follows the foundation model paradigm, where large-scale unsupervised or self-supervised learning develops generalizable representations that support diverse downstream tasks. The multimodal nature of the pre-training data enables development of cross-modal representations that integrate visual, linguistic, tactile, and action information.

##### 3.1.2.2 Scaling Law Application in Embodied Intelligence

The AWE2.0 development explicitly applies **scaling law principles to embodied intelligence**, testing whether performance improvements with model and data scale observed in language and vision extend to physical interaction domains . Dr. Ding Wenchao's statement about "paving the way for scaling laws in future embodied foundation models" indicates deliberate investigation of scaling relationships.

##### 3.1.2.3 Fine-Tuning for Specific Robotic Platforms (e.g., Embroidery Robots)

Following pre-training on general WIYH data, AWE2.0 undergoes **fine-tuning for specific robotic platforms and task domains** . The reported application to **embroidery robots** demonstrates this adaptation process, transferring general manipulation understanding to the specialized domain of precision fabric manipulation.

#### 3.1.3 Performance Characteristics

##### 3.1.3.1 Smooth Action Generation

AWE2.0 demonstrates **smooth action generation** that produces natural, efficient movement trajectories rather than jerky or discontinuous motion . This smoothness reflects learning from human demonstrations that inherently exhibit the efficiency and coordination characteristic of skilled performance.

##### 3.1.3.2 Real-World Deployment Efficacy

AWE2.0 has demonstrated **real-world deployment efficacy** in practical applications including embroidery robot control . This deployment success validates the training methodology and indicates that the model has developed robust capabilities that transfer from training data to operational contexts.

### 3.2 Training Paradigms for World Models in Embodied AI

#### 3.2.1 World Models 2: 2026 Developments

##### 3.2.1.1 Release Context: February 2026

The anticipated release of **World Models 2 in February 2026** represents a significant milestone in predictive models for embodied AI . This release builds upon foundational work in world modeling and responds to growing recognition that predictive understanding is essential for sample-efficient learning and robust decision-making.

##### 3.2.1.2 Potential Architectural Innovations (Under Investigation)

While specific architectural details remain under investigation, potential innovations include: **extended prediction horizons through improved temporal abstraction**, **enhanced multimodal prediction** generating consistent predictions across vision, language, and proprioceptive modalities, and **integration of symbolic or structured representations** supporting explicit reasoning about physical constraints .

#### 3.2.2 Integration of World Models with Embodied Control

##### 3.2.2.1 Predictive State Representation Learning

The integration centers on **learning predictive state representations** that capture information relevant for future decision-making . These representations compress high-dimensional sensory observations into compact latent states that support efficient prediction and planning.

##### 3.2.2.2 Action-Conditional Future Prediction

**Action-conditional future prediction** enables world models to support planning and decision-making by predicting consequences of hypothetical actions . This capability allows evaluation of action alternatives without physical execution.

##### 3.2.2.3 Model-Based Reinforcement Learning for Robotics

**Model-based reinforcement learning (MBRL)** leverages world models to enable sample-efficient policy learning through imagined experience . In MBRL, the world model generates synthetic trajectories that supplement real-world interaction data, dramatically reducing required physical trials.

### 3.3 Cross-Methodological Training Approaches

| Training Approach            | Description                                          | Key Data Requirements                    | Representative Applications    |
| :--------------------------- | :--------------------------------------------------- | :--------------------------------------- | :----------------------------- |
| **Self-supervised learning** | Learning from data structure without explicit labels | Large-scale multimodal demonstrations    | Representation pre-training    |
| **Imitation learning**       | Direct replication of expert demonstrations          | High-quality expert trajectories         | Behavioral cloning, inverse RL |
| **Reinforcement learning**   | Learning from environmental feedback                 | Reward signals, safety constraints       | Policy fine-tuning, adaptation |
| **Hybrid training**          | Simulation pre-training + real-world fine-tuning     | Simulation environment + real-world data | Sim-to-real transfer           |

#### 3.3.1 Self-Supervised Learning from Multimodal Demonstrations

**Self-supervised learning** extracts supervision signals from the inherent structure of demonstration data without requiring explicit reward or success labels . Objectives include predicting future observations, reconstructing masked inputs, and learning cross-modal correspondences.

#### 3.3.2 Imitation Learning with Human-Centric Data

**Imitation learning** directly trains policies to replicate expert demonstrations, providing a straightforward path from data collection to capable policies . Behavioral cloning trains policies to predict expert actions from observations, while more sophisticated approaches address multimodal behavior and compounding errors.

#### 3.3.3 Reinforcement Learning from Real-World Feedback

**Reinforcement learning from real-world feedback** enables continued policy improvement beyond demonstration capabilities . World models play a critical role in enabling sample-efficient real-world RL through imagined experience and predictive safety evaluation.

#### 3.3.4 Hybrid Training: Simulation Pre-training + Real-World Fine-Tuning

**Hybrid training** combines simulation pre-training with real-world fine-tuning, leveraging scalability and safety of simulation with accuracy of real-world data . This approach has become standard practice in embodied AI.

## 4. Technical Foundations and Related Research (2025–2026)

### 4.1 Core Technologies Enabling Large-Scale Data Collection

#### 4.1.1 Wearable Sensor Systems for Embodied Data Capture

##### 4.1.1.1 SenseHub Platform (TARS Robotics)

The **SenseHub platform** integrates multiple sensor types in a wearable configuration that follows natural human movement . The architecture includes distributed sensor nodes for visual capture, tactile sensing, and motion tracking, with sophisticated hardware engineering for temporal synchronization and spatial registration.

##### 4.1.1.2 13+ Sensor Types in WIYH Dataset

The WIYH dataset incorporates **more than 13 distinct sensor types**, providing comprehensive coverage of information streams relevant for embodied intelligence . This sensor diversity captures the rich multimodal structure of physical interaction.

#### 4.1.2 Teleoperation Interfaces and Controllers

##### 4.1.2.1 GELLO Controller Design (OpenAI)

The **GELLO controller** provides an ergonomic master interface mapping human hand movements to robot end-effector commands . The 3D-printed construction enables low-cost, rapid deployment.

##### 4.1.2.2 Low-Cost 3D-Printed Hardware Solutions

**Low-cost 3D-printed hardware** has emerged as an enabling technology for scalable teleoperation infrastructure, reducing per-station cost from tens of thousands to hundreds of dollars .

### 4.2 Automated Data Processing Pipelines

| Processing Stage              | Function                                 | Key Technologies                                 |
| :---------------------------- | :--------------------------------------- | :----------------------------------------------- |
| **Real-time synchronization** | Align multimodal sensor streams          | Timestamp-based alignment, clock synchronization |
| **Automated annotation**      | Generate structured labels from raw data | Foundation models, computer vision, NLP          |
| **Quality control**           | Filter anomalous or low-quality data     | Statistical methods, learned quality predictors  |

#### 4.2.1 Real-Time Multimodal Synchronization

**Real-time multimodal synchronization** aligns sensor streams with diverse sampling rates and latency characteristics, essential for meaningful multimodal fusion .

#### 4.2.2 Automated Annotation and Label Generation

**Automated annotation** converts raw sensor data into structured training examples without manual intervention, enabling dataset scale that would be economically infeasible otherwise .

#### 4.2.3 Quality Control and Data Filtering Mechanisms

**Quality control mechanisms** identify and exclude anomalous data through statistical and learned methods, maintaining dataset utility at scale .

### 4.3 Academic and Industry Research Landscape

#### 4.3.1 Key Research Institutions and Corporate Labs (2025–2026)

| Organization      | Location           | Focus                             | Key Contribution                     |
| :---------------- | :----------------- | :-------------------------------- | :----------------------------------- |
| **TARS Robotics** | Shanghai, China    | Human-centric data infrastructure | WIYH dataset, SenseHub, AWE2.0       |
| **OpenAI**        | San Francisco, USA | Large-scale teleoperation         | Robotics lab, GELLO-based collection |
| **DeepMind**      | London, UK         | World models, generalist agents   | Genie 3, Gemini Robotics             |
| **NVIDIA**        | Santa Clara, USA   | Simulation, physical AI           | Cosmos platform                      |

##### 4.3.1.1 TARS Robotics (Shanghai, China)

TARS Robotics has established itself as a **data infrastructure specialist** with open-access distribution, positioning for ecosystem development .

##### 4.3.1.2 OpenAI (San Francisco, USA)

OpenAI applies **substantial capital resources to proprietary data collection** at unprecedented scale, with commitment to continued infrastructure expansion .

##### 4.3.1.3 Emerging Players in Embodied AI Data Infrastructure

Additional organizations including **DeepMind, NVIDIA, and various startups** are contributing to rapid ecosystem development with diverse technical approaches .

#### 4.3.2 Publication Venues and Preprint Trends

##### 4.3.2.1 arXiv Robotics and AI Preprints

**arXiv preprints** have become the primary channel for rapid dissemination, with substantial embodied AI activity including TARS Robotics' technical documentation .

##### 4.3.2.2 Conference Proceedings: ICRA, IROS, CoRL, NeurIPS

**Major conferences** including ICRA, IROS, CoRL, and NeurIPS provide peer-reviewed publication paths with emphasis on physical system validation and algorithmic innovation .

## 5. Challenges and Future Directions

### 5.1 Current Limitations in Dataset Construction

#### 5.1.1 Cost and Scalability of Human-Centric Collection

Despite progress, **human-centric data collection remains expensive and difficult to scale**. Operational costs of large-scale collection run to millions of dollars annually, constraining participation to well-funded organizations . Scalability challenges extend beyond direct costs to human operator availability, training requirements, and fatigue management.

#### 5.1.2 Sim-to-Real Gap Persistence

**The sim-to-real gap remains persistent** despite increased real-world data emphasis. Simulation continues to offer unique advantages for dangerous, rare, or counterfactual scenarios, requiring continued methodological innovation for effective integration .

#### 5.1.3 Data Privacy and Ethical Considerations

**Large-scale collection of human activity data raises significant privacy and ethical considerations**. Wearable recording in commercial settings captures potentially sensitive information requiring informed consent, appropriate anonymization, and careful misuse prevention .

### 5.2 Emerging Trends in Training Methodologies

#### 5.2.1 Foundation Model Approaches for Embodied AI

**Foundation model approaches** have become dominant, with large-scale pre-training on diverse data followed by task-specific adaptation proving effective across multiple embodied AI applications .

#### 5.2.2 Lifelong Learning and Continual Adaptation

**Lifelong learning and continual adaptation** enable systems to incorporate new experience without catastrophic forgetting, essential for deployment in evolving environments .

#### 5.2.3 Cross-Modal Transfer and Generalization

**Cross-modal transfer and generalization** leverage multimodal dataset structure to develop representations that support flexible deployment across varying sensory configurations .

### 5.3 Anticipated Developments for 2026 and Beyond

#### 5.3.1 Expansion of Open-Source Dataset Ecosystems

The **open-source release of WIYH suggests continued expansion** of publicly available embodied datasets, with community governance structures enabling collaborative development .

#### 5.3.2 Standardization of Evaluation Protocols

**Standardized evaluation protocols** are increasingly important as dataset and model diversity grows, enabling meaningful comparison across research efforts .

#### 5.3.3 Integration of Large Language Models with Embodied Control

**Integration of large language models with embodied control** represents a major frontier, leveraging linguistic knowledge for task specification, planning, and human-robot interaction .

## 6. Conclusion

### 6.1 Summary of Key Advances in 2025–2026

The period 2025–2026 has witnessed **transformative advances in embodied AI data infrastructure**, centered on two major developments: **TARS Robotics' WIYH dataset** (100,000+ real-world VLTA multimodal demonstrations, open-access December 2025) and **OpenAI's large-scale teleoperation facility** (~100 collectors, 24/7 operation). Key innovations include: **(1) human-centric wearable data collection paradigms** that capture authentic expert performance in operational environments; **(2) comprehensive multimodal integration** (vision-language-tactile-action) enabling richer learning signals than prior approaches; **(3) fully automated annotation pipelines** that achieve dataset scale previously infeasible; and **(4) convergence of world models with embodied control** enabling predictive planning and sample-efficient learning.

### 6.2 The Path Toward Scalable Embodied Intelligence

The path forward requires **continued scaling of data infrastructure** while addressing cost, privacy, and diversity challenges. The complementary strengths of human-centric wearable collection (authenticity, environmental diversity, multimodal richness) and large-scale teleoperation (robot-actionability, collection control, operational intensity) suggest that **hybrid approaches combining both methodologies** may prove optimal. World model integration offers promise for reducing real-world data requirements through imagined experience, but depends on continued advances in predictive accuracy and long-horizon coherence.

### 6.3 Implications for Research and Industry Practice

For **researchers**, the availability of WIYH and comparable resources enables participation in embodied foundation model development without prohibitive data collection investment. For **industry practitioners**, the demonstrated commercial applications (embroidery robots, logistics automation) validate near-term economic value, while the scaling law framework provides guidance for resource allocation. The **open-source versus proprietary tension**—exemplified by TARS's open-access strategy versus OpenAI's internal collection—will continue to shape competitive dynamics and ecosystem development. Ultimately, the 2025–2026 advances establish the **data infrastructure foundation** upon which the next generation of capable, generalizable embodied intelligent systems will be built.