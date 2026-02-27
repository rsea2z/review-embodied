# Writing Guide: Comprehensive Survey on [Topic]

> **Template Source**: Derived from *"A Comprehensive Survey on World Models for Embodied AI"* (Li et al., 2025).
> **Purpose**: Use this template to structure high-quality academic surveys in AI/Robotics.
> **Style Note**: Maintain an authoritative, objective, and dense academic tone. Use active voice for contributions ("We propose...", "We introduce...") and passive/neutral for literature review ("...has been proposed", "...can be instantiated").

---

## Title
**[A Comprehensive Survey on [Topic] for [Domain]]**

---

## Abstract
*Maximum 200-250 words. Single paragraph with precise structure.*

**Structure (in order)**:
1. **Context Sentence**: Start with the high-level domain goal
   - *Pattern*: "[Domain] requires agents that [core capability]. [Topic/Concept] serves as [functional role]."
   - *Example*: "Embodied AI requires agents that perceive, act, and anticipate how actions reshape future world states. World models serve as internal simulators that capture environment dynamics..."

2. **Problem Formulation**: Define what you formalize
   - *Pattern*: "This survey [presents/introduces] a unified framework for [Topic]."
   - *Sub-pattern*: "Specifically, we formalize the problem setting and [learning objectives/core concepts]..."

3. **Taxonomy Statement**: State your classification axes
   - *Pattern*: "...and propose a [N]-axis taxonomy encompassing: (1) [Axis 1, Definition]; (2) [Axis 2, Definition]; (3) [Axis 3, Definition]."
   - **Critical**: Number your axes and provide brief inline definitions

4. **Scope Coverage**: List what you systematize
   - *Pattern*: "We systematize data resources and metrics across [Domain 1], [Domain 2], and [Domain 3], covering [metric type 1], [metric type 2], and [metric type 3]."

5. **Comparative Analysis**: Mention quantitative contributions
   - *Pattern*: "Furthermore, we offer a quantitative comparison of state-of-the-art models and distill key open challenges..."
   - *Example*: "...including [challenge 1], [challenge 2], and [challenge 3]."

6. **Resource Contribution**: Conclude with reproducibility link
   - *Pattern*: "Finally, we maintain a curated bibliography at [URL]."

**Example Flow**:
> Embodied AI requires agents that perceive complex, multimodal environments, act within them, and anticipate how their actions will alter future world states. World models serve as internal simulators capturing environment dynamics to support perception, prediction, and decision making. This survey presents a unified framework for world models in embodied AI. Specifically, we formalize the problem setting and propose a three-axis taxonomy: (1) Functionality, distinguishing Decision-Coupled vs. General-Purpose models; (2) Temporal Modeling, contrasting Sequential vs. Global prediction; (3) Spatial Representation, spanning latent vectors to explicit geometry. We systematize data resources and metrics across robotics, autonomous driving, and general video, covering pixel prediction quality, state-level understanding, and task performance. Furthermore, we provide quantitative comparisons and distill key challenges. Finally, we maintain a curated bibliography at [URL].

---

## Index Terms
[Primary Keyword 1], [Primary Keyword 2], [Core Topic], [Application Domain].

---

## 1. Introduction

*Goal: Hook reader → contextualize problem → position contribution → outline structure.*

### 1.1 Hook & Definition
**Opening paragraph—establish the field's high-level goal**:
- *Pattern*: "[Field/Domain] aims to equip agents to [capability 1], [capability 2], and [capability 3]."
- *Style*: Broad, aspirational, and grounded in application.

**Focus paragraph—narrow to your core subject**:
- *Pattern*: "Central to this capability is [Topic]. This survey focuses on [Topic] that [inclusion criteria], distinguishing them from [related but excluded concepts]."
- *Implementation*: Create a clear boundary between what you survey and what you don't. Use a sentence to explicitly exclude related work (e.g., "We focus on controllable dynamics models, distinguishing them from static scene descriptors or purely generative visual models.").

### 1.2 Motivation & History
**Cognitive/Theoretical Basis (1-2 paragraphs)**:
- Begin with grounding in adjacent discipline (cognitive science, control theory, physics, etc.)
- *Pattern*: "[Discipline] suggests [principle]. Motivated by this view, early AI research..."
- *Style*: Use citations to foundational cognitive/scientific work to elevate your topic.

**Historical Evolution (1-3 paragraphs)**:
- Trace from early seminal work → intermediate developments → modern breakthroughs
- *Pattern*: "The seminal work of [Author] crystallized the term '[Topic]' and inspired [subsequent work]. More recently, advances in [Trend 1] and [Trend 2] have expanded [Topic] beyond [initial scope] into [new scope]."
- **Key Technique**: End each evolutionary step with a brief consequence or enabling insight.
- *Example Structure*:
  - Sentence 1: Introduce foundational work and what it established
  - Sentence 2-3: Trace technical progression (e.g., RNN → Transformer → Diffusion)
  - Sentence 4: Connect to modern generative paradigm or application expansion

### 1.3 Problem Statement (The "Why Now?")
**Complexity/Challenge (1 paragraph)**:
- Explain why your topic is fundamentally hard to solve
- *Pattern*: "Faithfully capturing [phenomenon] requires addressing both [challenge X] and [challenge Y]. [Challenge X] establishes [specific problem] as a central challenge..."
- *Style*: Be specific about technical barriers (long-horizon coherence, sim-to-real gap, computational efficiency trade-offs).

**Gap Analysis (1-2 paragraphs)**:
- Acknowledge existing surveys and systematically critique them
- *Pattern*: "Several recent surveys [have organized/surveyed] this literature. Overall, these surveys follow [Approach 1] and [Approach 2]. However, [Critique 1]. Furthermore, [Critique 2]."
- *Critique Examples*:
  - Too narrow in scope (e.g., only robotics, ignoring driving)
  - Inconsistent taxonomy (mixing functional and architectural dimensions)
  - Outdated (pre-generative AI era)
  - Focus on different axis than needed (e.g., application-driven vs. method-driven)

### 1.4 Contributions (This Survey)
**Unified Framework Introduction (1 paragraph)**:
- *Pattern*: "To address [the gap/the lack of], this work introduces a framework centered on [N] core axes [or "core design dimensions"]..."
- **Critical Detail**: Explicitly state your axes here and their motivation.
- *Example*: "...centered on three core axes: Functionality (decision-coupling), Temporal Reasoning (sequential vs. global), and Spatial Representation (latent to explicit geometry)."

**Benefits of Framework (1 paragraph)**:
- Standardization: Why is unification needed?
- Roadmap: How does it guide future research?
- Comparison: What does it enable?

**Structural Roadmap (1 paragraph)**:
- *Pattern*: "Fig. [X] presents an overview of the survey structure. We begin in §[N] by [brief description]. §[N+1] introduces [description]. [...]. §[Final] concludes with [outlook]."
- **Visualization Note**: Mention your main organizing figure early and reference it throughout.

---

## 2. Background

*Goal: Establish mathematical/conceptual foundation so any reader can understand subsequent taxonomy.*

### 2.1 Core Concepts
**Functional Pillars (1-2 subsections)**:
- Break your domain into 3-4 core functional components
- *Pattern*: "The functionality of [Topic] rests on [N] aspects: ..."
- Use bulleted breakdown for clarity:
  - **[Pillar 1]**: [Definition and role]
  - **[Pillar 2]**: [Definition and role]
  - **[Pillar 3]**: [Definition and role]
  
**Example from World Models**:
> "Its functionality rests on three aspects:
> - **Simulation & Planning**: Uses learned dynamics to generate plausible futures, enabling imagination-based planning.
> - **Temporal Evolution**: Learns how encoded states evolve, enabling temporally consistent rollouts.
> - **Spatial Representation**: Encodes scene geometry at appropriate fidelity using latent tokens or neural fields."

### 2.2 Mathematical Formulation
**Formalism & Notation (0.5 pages)**:
- Introduce standard formalism for your domain (e.g., POMDP, MDP, VAE, Diffusion framework)
- *Pattern*: "We formalize the environment interaction as a [standard formalism]."
- Define key symbols and variables clearly

**Core Equations (1-2 pages)**:
- **Equation 1**: Dynamics Prior / Initial Distribution
- **Equation 2**: Likelihood / Observation Model / Joint Distribution
- **Equation 3**: Posterior / Inference Model
- **Equation 4**: Optimization Objective (e.g., ELBO, VAE loss)
- *Style*: Use numbered equations. Provide brief inline explanation after each.

**Modern Architecture Connection (0.5 pages)**:
- Bridge classical formalism to modern architectures
- *Pattern*: "Modern [Topic] implementations adopt a [paradigm] training approach. These models can be instantiated with [architecture option 1], [option 2], or [option 3], where the learned [latent representation] serves as..."
- *Example*: "Modern world models thus adopt a reconstruction–regularization training paradigm: the likelihood term encourages faithful observation prediction, and KL regularization aligns the filtered posterior with the dynamics prior. Such models can be instantiated with recurrent models, Transformer-based architectures, or diffusion-based decoders."

---

## 3. Taxonomy (Core Contribution)

*Goal: Present your classification system with clarity. This section is the heart of the survey.*

### Overview
**Meta-statement on categorization (1 paragraph)**:
- *Pattern*: "We categorize [Topic] along [N] core dimensions, which provide the foundation for the subsequent analysis."
- **Key Detail**: State why these specific dimensions matter (e.g., "they fundamentally influence [outcome 1], [outcome 2], and [outcome 3]").

**Axis Definitions (1 paragraph per axis)**:
- *Pattern*: "The [ordinal]-axis, [axis name], [distinguishes/delineates] [Category A] from [Category B]. [Category A] are [definition/characteristic]. In contrast, [Category B] [definition/characteristic]."
- **Critical**: Provide contrastive definitions. Make the distinction binary or clearly enumerated.

### 3.1 [Axis 1: e.g., Functionality / Decision Coupling]

**Overview of categories** (1 short paragraph):
- List the categories under this axis

**[Category 1.A]** (1-2 pages):
- **Definition**: Clear, one-sentence definition
- **Mechanism**: How does it work? What's the design principle?
- **Representative Works**: [Citation 1], [Citation 2], [Citation 3]... (use inline citations, organize chronologically or by sub-type)
- **Design Variants**: Any important sub-variants? (e.g., within RNN-based approaches, RSSM vs. IDM)
- **Trade-offs**: What does this approach gain/lose? (e.g., efficiency vs. fidelity)

**[Category 1.B]** (1-2 pages):
- Same structure as 1.A

### 3.2 [Axis 2: e.g., Temporal Modeling]

**Overview** (1 short paragraph):
- Explain the distinction and why it matters for long-horizon consistency or efficiency

**Sequential Simulation and Inference** (1-2 pages):
- *Definition*: Autoregressively unfolds future states one step at a time
- *Mechanism*: Markov assumption, sequential conditioning, recurrent or masked-causal Transformer
- *Works*: Organize by sub-category if useful (e.g., RNN-based, Transformer-based, Diffusion-based)
- *Example paragraph structure*:
  > "Sequential approaches unroll predictions step-by-step. [Work A] introduced [mechanism], which [consequence]. Building on this, [Work B] [improvement]. Recent advances employ [modern architecture] to [capability]..."

**Global Difference Prediction** (1-2 pages):
- *Definition*: Predicts entire future trajectories in parallel via masked or generative modeling
- *Mechanism*: Masked prediction, global diffusion, parallel decoding
- *Works*: Organize similarly

### 3.3 [Axis 3: e.g., Spatial Representation]

**Overview & Typology** (1 paragraph):
- *Pattern*: "Spatial representation comprises [N] primary strategies. We categorize them by [encoding granularity / explicitness / dimensionality]..."

**[Representation 3.A: e.g., Global Latent Vector]** (0.5-1 page):
- **Characteristics**: Encodes complex states into compact vectors; efficient for real-time control
- **Works**: Early examples → modern refinements
- **Trade-offs**: Efficiency ↔ Fine-grained spatial detail

**[Representation 3.B: e.g., Token Feature Sequences]** (1 page):
- **Characteristics**: Discrete tokens, supports multimodal fusion, reuses LLM infrastructure
- **Works**: RSSM-token variants, Transformer-token models, LLM integration
- **Recent Trends**: CoT reasoning, VLM integration

**[Representation 3.C: e.g., Spatial Latent Grids]** (1 page):
- **Characteristics**: Geometry-aligned (BEV, voxel grids); preserves spatial locality; enables efficient convolutional/attention operations
- **Works**: Organized by domain (driving, navigation, manipulation)
- **Advantages**: Geometric priors, streaming rollouts, planner-ready outputs

**[Representation 3.D: e.g., Decomposed Rendering (NeRF, 3DGS)]** (1 page):
- **Characteristics**: Explicit 3D primitives (neural fields, Gaussians) updated to simulate dynamics
- **Works**: NeRF-based, 3DGS-based, hybrid approaches
- **Advantages**: View-consistent synthesis, object compositionality, geometry fidelity
- **Challenges**: Computational cost, long-horizon stability

### Summary Tables
**Table [N-1]: Robotics and General-Purpose Methods**:
- **Columns**: Paper, Publication Venue, Taxonomy Class (Format: Dec/Seq/GLV or Gen/Glo/DRR), Core Architecture/Approach, Datasets Used (DMC, Meta-World, RLBench, etc.), Input Modality (RGB, Proprioception, Depth, etc.), Real-World Validation (✓ or blank)
- **Organization**: Group by taxonomy class for clarity; sort chronologically within groups
- **Annotation**: Underline newly proposed or aggregated datasets to highlight data contributions

**Table [N-2]: Autonomous Driving Methods**:
- **Columns**: Paper, Publication, Taxonomy Class, Core Architecture, Datasets (CARLA, nuScenes, Waymo, etc.), Input Modality (RGB, LiDAR, Motion, Maps, Occupancy), Real-World Validation
- **Key Insight**: Show how world models distribute across driving-specific metrics and datasets

**Tips for Tables**:
- Make column headers concise; use abbreviations
- Use check marks (✓) for binary attributes; avoid text-heavy cells
- Group rows by taxonomy dimension for visual scanning
- Highlight outlier or particularly impactful papers (bold, shading, or footnotes)

---

## 4. Data Resources & Metrics

*Goal: Standardize evaluation. Readers need clear guidance on reproducibility and comparison.*

### 4.1 Datasets

**Organization by Category**:
1. **Simulation Platforms**: Controllable, scalable, deterministic
2. **Interactive Benchmarks**: Standardized tasks with closed-loop protocols
3. **Offline Datasets**: Large-scale pre-collected trajectories for pretraining
4. **Real-World Platforms**: Physical robot systems

**For Each Dataset/Platform**:
- **Name & Citation**: [Full citation]
- **Domain**: (e.g., Robotics, Autonomous Driving, General Video)
- **Type**: (Sim / Benchmark / Offline / Real)
- **Task Coverage**: What tasks or domains does it enable?
- **Modality**: RGB, LiDAR, Proprioception, Text, Depth, etc.
- **Scale**: Approx. number of trajectories, hours of video, or task count
- **Key Characteristic**: What makes it valuable? (e.g., "photorealistic rendering", "sparse reward", "multi-task")

**Example Subsection**:
> **4.1.1 Simulation Platforms**
> - **MuJoCo**: Physics engine; articulated systems; widely used for control benchmarks
> - **CARLA**: Autonomous driving; photorealistic rendering; closed-loop evaluation
> - **Isaac Ecosystem**: GPU-accelerated; large-scale RL; robotics and driving

### 4.2 Evaluation Metrics

**Organize by Evaluation Dimension**:

1. **Visual Quality Metrics**:
   - **PSNR, SSIM**: Pixel-level reconstruction fidelity
   - **FID, FVD**: Perceptual quality and temporal coherence (for video)
   - **LPIPS**: Learned perceptual similarity
   - *Use Case*: Assessing prediction realism and fidelity

2. **State-Level / Geometric Consistency**:
   - **3D Reconstruction Error** (Chamfer distance, L2 on occupancy)
   - **Optical Flow Error**: Motion consistency
   - **Geometric Consistency**: View-consistency, multi-frame alignment
   - *Use Case*: Ensuring physical realism beyond pixel appearance

3. **Physics & Control Metrics**:
   - **Task Success Rate**: Percentage of successful downstream task executions
   - **Reward on Downstream Tasks**: Proxy for behavioral correctness
   - **Sample Efficiency**: Data needed to reach performance threshold
   - *Use Case*: Measuring actionability for embodied agents

4. **Long-Horizon & Stability**:
   - **Prediction Horizon**: How many steps consistent? (measured in steps or seconds)
   - **Error Accumulation Rate**: How quickly does error grow?
   - **Temporal Consistency Score**: Optical flow, point tracking across frames
   - *Use Case*: Assessing model robustness for long-horizon planning

5. **Domain-Specific Metrics**:
   - **Autonomous Driving**: Collision rate, lane-keeping accuracy, trajectory ADE/FDE
   - **Manipulation**: Grasp success, trajectory smoothness, object-state accuracy
   - **Navigation**: Success weighted by path length, exploration coverage
   - *Use Case*: Application-specific performance evaluation

**Critical Guidance**:
- *Pattern*: "Faithful evaluation requires metrics across [dimension 1], [dimension 2], and [dimension 3], as no single metric captures [phenomenon]."
- *Example*: "Faithful evaluation requires metrics across visual quality, state-level understanding, and task performance, as no single metric captures the interplay between prediction fidelity and downstream agent performance."

---

## 5. Performance Comparison & Quantitative Analysis

*Goal: Provide evidence of SOTA landscape and trade-off analysis.*

### Overview (1 paragraph)
- Summarize how you organize comparisons (by domain, by taxonomy class, etc.)
- Acknowledge data constraints (not all papers report all metrics)

### Comparisons by Taxonomy Class
**For each major taxonomy combination** (e.g., "Decision-Coupled + Sequential + GLV"):
- **Representative Models**: List 3-5 papers
- **Key Metrics**: Report SOTA numbers on standard benchmarks (e.g., average FVD on SSv2, success rate on Meta-World)
- **Trade-offs**: Compare computation cost vs. accuracy, sample efficiency vs. fidelity, etc.

### Cross-Domain Analysis
- **Robotics vs. Autonomous Driving**: How do design choices differ? Why?
- **Simulation vs. Real-World Gap**: Quantify S2R transfer success rates
- **Generalist vs. Specialist**: Compare general-purpose models against domain-specific tuned approaches

### Graphical Comparisons
- **Scatter plot**: E.g., Model Complexity (parameters) vs. Performance (FVD or Success Rate)
- **Radar/Spider chart**: Multi-metric comparison across 4-5 dimensions
- **Timeline**: Evolution of SOTA metrics over years
- **Trade-off curves**: Pareto frontier of Speed vs. Quality, Memory vs. Accuracy, etc.

---

## 6. Challenges and Open Directions

*Goal: Identify real bottlenecks and future research opportunities.*

### Fundamental Challenges (Phenomena, Not Just Engineering)

**Challenge 1: [e.g., Long-Horizon Temporal Consistency]** (1-2 paragraphs)
- *Problem Statement*: Why is this hard? What's the root cause?
- *Current Solutions*: How are recent methods attempting to address it?
- *Remaining Gap*: What's insufficient about current approaches?
- *Metrics*: How would you measure progress?

**Challenge 2: [e.g., Real-Time Efficiency vs. Fidelity Trade-off]** (1-2 paragraphs)
- Same structure

**Challenge 3: [e.g., Sim-to-Real Gap / Dataset Scarcity]** (1-2 paragraphs)
- Same structure

### Emerging Trends & Research Directions

**Trend 1: [e.g., Generative AI Integration / Foundation Models]** (1 paragraph)
- *Opportunity*: What becomes possible?
- *Key Works*: [Citations]
- *Open Questions*: What's unresolved?

**Trend 2: [e.g., Multimodal World Models with VLMs/LLMs]** (1 paragraph)
- Same structure

**Trend 3: [e.g., Explicit Physics Inductive Biases]** (1 paragraph)
- Same structure

### Domain-Specific Bottlenecks
- **Robotics**: E.g., contact modeling, deformable objects, real-time constraints
- **Autonomous Driving**: E.g., interactive agents, rare events, long-horizon stability
- **General Video**: E.g., semantic understanding, compositional reasoning

---

## 7. Conclusion & Outlook

### Recap (1 paragraph)
- Summarize the state of the field (SOTA approaches, dominant paradigms)
- Reiterate how your taxonomy unifies disparate approaches

### Value of the Framework (1 paragraph)
- How does your taxonomy enable clearer thinking?
- *Pattern*: "This taxonomy clarifies [dimension], enables [capability], and guides [research direction]."

### Future Outlook (1-2 paragraphs)
- Synthesize challenges into a vision for the next era of research
- *Pattern*: "The next generation of [Topic] will likely integrate [trend 1], address [challenge 1], and require [resource/methodology]."
- **Aspirational Ending**: End with a compelling vision that motivates continued work in your field

### Closing Statement
- One sentence capturing the significance or inevitability of progress in your domain

---

## Writing Style & Execution Guidelines

### Paragraph Structure (Critical)
**Each paragraph should follow this pattern**:
1. **Topic Sentence**: State the main claim or context
2. **Evidence/Examples**: Support with citations and specific methods
3. **Synthesis**: Connect back to your framework or draw implications
4. **Transition**: Bridge to next paragraph or section

**Example Paragraph**:
> "Early sequential models employed RNNs to capture temporal dependencies. Ha and Schmidhuber [9] introduced the first world model by encoding observations into latent space and using RNNs for dynamics modeling. PlaNet [38] refined this with the Recurrent State-Space Model (RSSM), fusing deterministic and stochastic components. These foundational architectures (RSSM, Dreamer, DreamerV2) establish the classical paradigm for sequential simulation and continue to inspire modern research."

### Citation & Reference Style
- **Use numbered citations**: `[1], [2], [3]` (not author-date)
- **Group related citations**: `[1], [2], [3]` for similar works or series papers
- **Cite strategically**: 
  - Early foundational work (establish lineage)
  - Recent SOTA (show progress)
  - Related but excluded work (boundary-setting)
  - Comparative benchmarks (evidence)

### Technical Vocabulary
**Use precise terms consistently**:
- "World model" (vs. "dynamics model", "forward model"—reserve latter for specific subtypes)
- "Latent dynamics", "counterfactual rollout", "sample efficiency"
- "State-space model", "variational approximation", "reconstruction loss"
- **Bold key terms** on first introduction: "We employ **masked autoencoder** for..."

### Formatting Best Practices
- **Math**: LaTeX for all equations; number sequentially
- **References**: Author names and years in appendix; inline citations via numbers
- **Figures**: 
  - Fig. 1 (structural overview of taxonomy): Place early, reference throughout
  - Fig. 2, 3, etc. (example architectures, methods): Place within sections
  - Captions: Informative (2-3 sentences), stand-alone readable
- **Tables**:
  - Table I, II (comprehensive method classification): Core contribution
  - Table III (datasets/benchmarks): Reference material
  - Use consistent abbreviations and column ordering
- **Section Cross-References**: Use `§2.1`, `§4.2` notation

### Tone & Authority
- **Objective & Balanced**: "Recent advances in [X] have [achieved Y], while [challenge Z] remains unresolved."
- **Avoid Hyperbole**: Don't claim "revolutionary" or "first-ever" unless thoroughly justified
- **Acknowledge Uncertainty**: "A promising direction is...", "While not yet mainstream, [approach] shows promise..."
- **Balance Criticism**: When critiquing prior surveys, be constructive: "While prior work organized methods by [dimension], we propose [alternative] to better capture [phenomenon]."

### Common Pitfalls to Avoid
1. **Over-long Taxonomy**: Limit to 2-4 primary axes; sub-categories should number ≤5 each
2. **Cherry-picked Papers**: Aim for comprehensive coverage; acknowledge that not all papers fit neatly
3. **Vague Categorization**: Every paper should have a clear slot in your taxonomy; use footnotes if edge cases
4. **Metric Confusion**: Define each metric; explain why it matters; note its limitations
5. **Disconnected Sections**: Each section should connect back to your central framework and contribution
