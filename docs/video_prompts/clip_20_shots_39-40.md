# 片段 20｜破晓与雨中的彩虹（剧本镜头 39–40）

- 成片区间：3:43–3:56。横屏 16:9，建议生成 **14 秒**，取约 13 秒，留约 1 秒剪辑余量。
- 片内安排：0–6.5 秒为 39 的城市远景，6.5–9 秒为 40 的楼宇间彩虹，9–14 秒为洛天依的侧脸反应。最终按 3:49 的唱句与可用画面剪接。
- 从 Wan 版 38 的低机位水洼和撑伞背影，沿视线向上的方向切至新生成的街道远景。用连续雨声连接；两张参考图用于统一造型与环境，不锁定首帧。
- 本段仍是黎明。明亮白天的全景留给公交离站后的独立尾镜。

## 参考图上传顺序

1. **图1 / Picture 1：洛天依外出造型**，`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低马尾、花饰和灰色风衣。设定图为同一角色的多视图。
2. **图2 / Picture 2：C 组黎明街道**，`MV/pictures/C_anime_pbr/10_dawn_city.png`。参考街道纵深、右侧高架、路灯、雨雾和淡彩虹。第一镜主要表现电车与晨光，彩虹留到第二镜。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi from <Picture 1>, with a silver-grey low ponytail, flower hair accessory and grey fabric trench coat. She carries an open transparent umbrella.
<Subject 2> is the rainy dawn street from <Picture 2>, with an elevated railway to the right, warm streetlights, distant high-rises and a faint rainbow.

summary:
[reference generation] A morning train crosses <Subject 2> as the rainy city brightens. A faint rainbow becomes visible between the buildings, followed by a quiet side view of <Subject 1> looking up at it.

retention_analysis:
<Subject 1> (appears in [Shot 3]): partially_preserved - Use the same character and outdoor outfit in one side view.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): partially_preserved - Keep the street layout and dawn palette. The rainbow becomes legible in the second shot. Keep the street soft in the close view.

detailed_description:
A semi-realistic Japanese anime city with PBR-like materials, visible fine rain and small patches of reflected light on wet paving.
[Shot 1] A single wide street view at <Subject 2>. The camera tilts gently upward from the wet street toward the high-rises. An illuminated morning commuter train travels along the elevated tracks on the right. Streetlamps still glow softly as a muted touch of gold reaches the pale blue-grey clouds. Hold the spatial continuity of the street and railway throughout the shot.
[Shot 2] At 00:06.500, cut to a wide view of the opening between distant buildings. A short, faint rainbow is visible against the rain haze. Hold long enough to read it while fine rain keeps falling.
[Shot 3] At 00:09.000, cut to a medium close side view of <Subject 1> on the sidewalk. Under her clear umbrella, she gently lifts her head and eyes toward the opening in the sky. Soft dawn light edges her silver-grey hair, flower accessory and umbrella rim. Her expression relaxes slightly. Hold through the end with rain visible beyond the canopy.

overall_soundscape: Continuous light rain, distant city ambience and a soft passing train. Close raindrops on the umbrella become audible in the final shot. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 14 秒的雨天黎明 MV 片段。洛天依的外貌、发型与灰色风衣参考图1。黎明街道、右侧高架铁路、路灯、雨雾及远处淡彩虹参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–6.5秒：同一个街道大远景缓缓上摇。前景是有局部水迹的湿润街道，右侧一列亮着窗灯的清晨电车沿高架轨道驶过。远处楼宇上方的蓝灰云层透出一点暖色晨光，路灯仍亮着柔和余晖。画面中能一直看见下落的细雨。
2. 镜头2 6.5–9秒：切到同一街区的远方楼宇。楼群间有一小段淡彩虹，在雨雾中若隐若现。镜头短暂停留，让观众看清洛天依接下来望向的方向。
3. 镜头3 9–14秒：切到街边洛天依的侧脸中近景。她自然撑着透明伞，轻轻抬头，目光落向彩虹，神情稍稍舒展。淡金晨光勾亮发丝、花饰和伞沿，伞外的雨丝仍清楚可见。让她在这个神情上停留片刻。

【音频风格】
细雨贯穿三个镜头，远处电车的声音轻轻经过。切到洛天依时，能听见几下近处雨点落在透明伞面。无对白，歌曲在后期衔接。

【运镜与核心约束】
第一镜保持一次平缓上摇，随后按彩虹远景、人物侧脸的次序切镜。晨光保持克制，远处淡彩虹清楚可见，雨始终在下。
```

## 剪辑衔接

- 已检查 `output/shot37-38_1118_120629.mp4` 的尾部画面。低处能看见水洼，洛天依撑伞背对镜头，街灯仍亮。新片段以相近的灰蓝色和雨声切向开阔街道。
- 彩虹本身由第二镜交代。眼底或伞面的彩虹反光属于可选后期细节，侧脸镜头以抬头和表情为主。
