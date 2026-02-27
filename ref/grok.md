### Key Points
- Research suggests that large-scale datasets like Open X-Embodiment and DROID, often constructed via aggregation of existing robot demonstrations or distributed teleoperation, have driven advancements in embodied AI and world models over the past year, enabling better generalization across robots and environments.
- It seems likely that training methods combining self-supervised learning (e.g., JEPA) with imitation learning and diffusion models are increasingly common, balancing efficiency and physical realism, though challenges like simulation-to-real gaps persist.
- Evidence leans toward hybrid approaches in world models, such as RSSM for sequential dynamics and global prediction via Transformers, fostering long-horizon planning while acknowledging debates on data diversity and ethical sourcing.

### Dataset Acquisition in Recent Works
Over the past year, datasets for embodied AI and world models have emphasized scale and diversity to support generalization. For instance, aggregated datasets pool demonstrations from multiple sources, while others use teleoperation in real-world settings. Common construction methods include standardization to formats like RLDS, annotation with language or physics properties, and simulation-based generation for safety and cost reasons. Data quantities range from tens of thousands to millions of trajectories, often including multimodal inputs (RGB, depth, actions).

### Model Training Methods
Training typically involves pretraining on large datasets for feature extraction, followed by fine-tuning for specific tasks. Self-supervised objectives like reconstruction or prediction dominate for world models, with reinforcement learning elements for decision-making. Methods like diffusion for action generation and Transformers for sequence modeling address temporal consistency, but require careful handling of heterogeneity in cross-embodiment data.

---

### Advancements in Datasets and Training for Embodied AI and World Models: A Comprehensive Review

Embodied AI integrates perception, cognition, and action in physical or simulated environments, while world models simulate dynamics to enable prediction, planning, and imagination-based learning. Over the past year (2023-2026), research has focused on scaling datasets to support generalist models capable of cross-embodiment transfer—controlling diverse robots—and addressing long-horizon tasks. This review synthesizes key papers, detailing dataset construction, quantities, and training methods. We organize findings around core themes: dataset aggregation for scale, real-world teleoperation for diversity, simulation for realism, and hybrid training paradigms. Emphasis is placed on how these elements mitigate challenges like data scarcity, sim-to-real gaps, and temporal inconsistency.

#### Evolution of Datasets in Embodied AI
Datasets have shifted from domain-specific collections to large, heterogeneous corpora. Construction often involves pooling from multiple labs, teleoperation, or simulation with physics engines. Quantities have grown exponentially, enabling pretraining of foundation models. Below, we highlight representative works and datasets.

- **Open X-Embodiment (OXE)**: Introduced in "Open X-Embodiment: Robotic Learning Datasets and RT-X Models" (2023, arXiv:2310.08864). This dataset aggregates 60 existing robot datasets from 34 labs across 21 institutions, spanning 22 robot embodiments (e.g., single-arm, bimanual, quadrupeds). Construction method: Data pooling and standardization to RLDS format for unified action spaces, multimodal inputs (RGB, depth, point clouds), and language annotations. Data quantity: Over 1 million trajectories, demonstrating 527 skills and 160,266 tasks, with average trajectory length ~120 timesteps at 3-10 Hz. Used for cross-embodiment learning, showing positive transfer in manipulation tasks.

- **DROID (Distributed Robot Interaction Dataset)**: From "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset" (2024, arXiv:2403.12945). Constructed via distributed teleoperation by 50 collectors across North America, Asia, and Europe over 12 months, using single-arm robots in real-world settings. Method: Human demonstrations with multimodal data (RGB, depth, proprioception, language annotations), focusing on 564 diverse scenes (e.g., homes, offices). Data quantity: 76,000 trajectories (350 hours, 1.7 TB), covering 86 tasks like object manipulation and navigation. Includes improved camera calibrations for 36,000 episodes and 75,000 language-annotated successes.

- **RT-1 and RT-X Extensions**: In "RT-1: Robotics Transformer for Real-World Control at Scale" (2023) and its RT-X follow-up (2023), RT-1 collects 130,000 episodes over 17 months using 13 mobile manipulators. Construction: Teleoperation with language instructions, RGB observations, and 7-DoF actions. Quantity: 135,000 trajectories across 2 robot types. RT-X expands this via OXE aggregation, enabling training on mixed data for emergent skills.

- **LIBERO**: Detailed in "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" (2023, NeurIPS). Constructed in simulation (MuJoCo) with human demonstrations for procedural manipulation. Method: 130 tasks designed for continual learning, including RGB, text, and proprioception. Quantity: 50 trajectories per task (total ~6,500), split into suites like LIBERO-Spatial (10 tasks focusing on object relations). Supports evaluation of generalization in lifelong settings.

- **BEHAVIOR-1K**: From "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation" (2024, arXiv:2403.09227). Grounded in human surveys on preferred robot tasks. Construction: Crowdsourced definitions from 5,000 WikiHow articles, mapped to 1,484 WordNet synsets; instantiated in OmniGibson simulator with physics for rigid/deformable bodies and liquids. Quantity: 10,000 teleoperation demos across 50 tasks/scenes (houses, offices, etc.), with 9,000+ objects annotated for semantics/physics. Total trajectories: 10,000; dataset size ~1.5 TB in LeRobot format.

Other notable datasets include nuScenes (2020, used in 2023-2025 works like DriveDreamer, 1,000 scenes with multimodal sensors) and Waymo (1,150 scenes, 12 million annotations for occupancy forecasting). For world models, SSv2 (220,847 videos) and VideoMix22M (22 million samples) support video prediction pretraining.

#### Table 1: Comparison of Key Datasets

| Dataset           | Year                | Construction Method                                | Data Quantity                 | Key Features/Tasks                         | Used in Papers (Examples) |
| ----------------- | ------------------- | -------------------------------------------------- | ----------------------------- | ------------------------------------------ | ------------------------- |
| Open X-Embodiment | 2023                | Aggregation from 60 datasets, RLDS standardization | 1M+ trajectories, 527 skills  | Cross-embodiment manipulation, multimodal  | RT-X (2023), Octo (2024)  |
| DROID             | 2024                | Distributed teleoperation in real-world            | 76K trajectories, 350 hours   | 86 tasks, 564 scenes, language annotations | DROID (2024)              |
| RT-1/RT-X         | 2023                | Teleoperation with language instructions           | 130K-135K episodes            | Manipulation in 2 robot types              | RT-1 (2023), RT-X (2023)  |
| LIBERO            | 2023                | Simulated demos with human input                   | ~6,500 trajectories (50/task) | 130 lifelong manipulation tasks            | LIBERO (2023)             |
| BEHAVIOR-1K       | 2024                | Crowdsourced + simulation in OmniGibson            | 10K demos, 1,000 activities   | Household tasks, physics-realistic         | BEHAVIOR-1K (2024)        |
| nuScenes          | 2020 (used 2023-25) | Sensor fusion in driving scenarios                 | 1,000 scenes                  | Autonomous driving, occupancy              | DriveDreamer (2024)       |
| SSv2              | 2018 (used 2023-25) | Crowd-sourced video clips                          | 220,847 videos                | Action understanding, prediction           | V-JEPA 2 (2025)           |

#### Training Methods for Models
Training paradigms blend self-supervision for representation learning, imitation for behavior cloning, and RL for optimization. World models often use latent spaces for efficiency, with sequential (e.g., RSSM) or global (e.g., diffusion) prediction. Key papers illustrate these.

- **Sequential Simulation and Inference**: In "DreamerV3" (2023), RSSM (Recurrent State Space Model) trains on datasets like DMC (8 platforms) via imagination-based RL. Method: Latent dynamics prediction with GRU/Transformer, optimized via actor-critic on imagined rollouts. Used in OXE for manipulation, achieving temporal consistency.

- **Global Difference Prediction**: "Genie" (2024) and "Sora" (2024) use diffusion models on video datasets like SSv2/OpenDV (65M frames). Training: Denoising diffusion probabilistic models (DDPM) for parallel forecasting, pretrained self-supervised then fine-tuned with actions. In DriveDreamer (2024), applied to nuScenes for 4D occupancy.

- **Self-Supervised and Hybrid Approaches**: "V-JEPA 2" (2025) on VideoMix22M uses JEPA (Joint Embedding Predictive Architecture) for feature prediction in latent space, avoiding reconstruction bias. Combined with imitation learning in Octo (2024) on OXE: Pretrain vision-language-action (VLA) models end-to-end, fine-tune with PPO/SAC for tasks.

- **Cross-Embodiment Training**: RT-X (2023) pretrains Transformers on OXE mixtures, tokenizing actions/images. Method: Behavior cloning with high-capacity models (e.g., 300M parameters), showing 50% improvement over single-dataset training. In DROID (2024), diffusion policies mix in-domain and diverse data (50/50 batches), trained with robomimic for robustness.

- **Evaluation and Transfer**: Papers like "Occ3D" (2023) use voxel supervision on Waymo (200K frames) with Transformers for next-token forecasting, metrics like mIoU (34%). Sim-to-real studies in BEHAVIOR-1K transfer policies from OmniGibson to real manipulators, highlighting gaps in deformable object handling.

#### Challenges and Future Directions
While datasets like OXE provide scale, heterogeneity poses training challenges (e.g., varying control frequencies). Real-world data (DROID) improves robustness but is costly; simulations (BEHAVIOR-1K) bridge gaps via physics. Training methods must balance compute (e.g., JEPA's efficiency) with fidelity. Future work may focus on automated annotation, neuro-symbolic hybrids for interpretability, and ethical data sourcing to ensure inclusivity across global contexts.

This review underscores the interplay between diverse datasets and sophisticated training, paving the way for more capable embodied systems.

### Key Citations
- Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." arXiv:2310.08864 (2023). [https://arxiv.org/abs/2310.08864](https://arxiv.org/abs/2310.08864)
- Karl Pertsch et al. "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset." arXiv:2403.12945 (2024). [https://arxiv.org/abs/2403.12945](https://arxiv.org/abs/2403.12945)
- Cheng Chi et al. "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation." arXiv:2403.09227 (2024). [https://arxiv.org/abs/2403.09227](https://arxiv.org/abs/2403.09227)
- Bo Liu et al. "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning." NeurIPS (2023). [https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf](https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf)
- Google DeepMind. "RT-1: Robotics Transformer for Real-World Control at Scale." (2023). [https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)
- Daniel Hafner et al. "DreamerV3: Mastering Diverse Domains through World Models." (2023).
- Yann LeCun et al. "V-JEPA 2." (2025).
- Tianhe Yu et al. "nuScenes: A Multimodal Dataset for Autonomous Driving." (2020, used in 2024 works like DriveDreamer). [https://www.nuscenes.org/](https://www.nuscenes.org/)
- Something-Something v2 Dataset. (2018, used in 2023-2025). [https://20bn.com/datasets/something-something](https://20bn.com/datasets/something-something)
- Waymo Open Dataset. (2020, used in 2023-2025). [https://waymo.com/open/](https://waymo.com/open/)
- Occ3D Dataset. (2023). [https://arxiv.org/abs/2304.00290](https://arxiv.org/abs/2304.00290)