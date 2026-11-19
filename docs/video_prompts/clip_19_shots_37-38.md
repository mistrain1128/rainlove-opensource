# 片段 19｜路灯下举伞与水洼倒影（剧本镜头 37–38）

## 片段信息

- 剧本成片区间：3:31–3:43；镜头 37 为 3:31–3:37，镜头 38 为 3:37–3:43。
- 建议设置：横屏 16:9，生成 **13 秒**；成片取约 12 秒，留约 1 秒剪辑余量。建议片内 0:00–0:06.5 为桥下举伞，0:06.5–0:13 为低机位水洼倒影；实际按歌曲和动作调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片是人物及场景视觉参考，不是固定首帧。
- 从天桥切到桥下人行道，省略下楼梯过程。人物先手持**已经打开、放低的透明伞**，再把它平稳举回头顶；不要求模型生成收伞、重新开伞或爬楼梯。
- 天色为由夜转晨的灰蓝色，路灯余晖仍有暖色；雨丝持续可见。伞沿少量水珠在暖光里短暂闪动，保持自然克制，不做夸张喷溅。
- 远处雨声与车流声连续。伞重新举起后，近处雨点重新落在伞面上；鞋尖经过浅水洼时有轻微踩水声。歌曲后期连续对齐，不生成对白或新配乐。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰、灰色布料风衣和深色鞋；多视图代表同一人。
2. **图2 / Picture 2 — C 组黎明街道**：`MV/pictures/C_anime_pbr/10_dawn_city.png`。参考湿润人行道、沿街暖灯、灰蓝晨色和路边紫阳花；只使用街边局部或调整景别，避免在本片段强制呈现参考图中的完整彩虹。
3. **图3 / Picture 3 — C 组小水洼**：`MV/pictures/C_anime_pbr/04_puddle.png`。只参考小而浅的水洼、湿地砖与水面反光；背景建筑不作为必须复制的地点，将水洼放在桥下人行道上。

两个模型版本按相同顺序上传。图2的晨景亮度仅供参考，本段仍偏灰蓝、城市灯光尚在；图3为质感参考，不当作固定画面。伞只是普通透明伞，不要求偏向某一侧。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory, a grey fabric trench coat and dark shoes.
<Subject 2> is the rainy street environment referenced from <Picture 2>, with wet sidewalk, warm lamps, hydrangeas and a cool grey-blue early-dawn atmosphere.
<Subject 3> is the small shallow puddle and wet paving referenced from <Picture 3>, relocated to the sidewalk near the pedestrian bridge.

summary:
[reference generation] On the sidewalk near the bridge at <Subject 2>, <Subject 1> lifts her already-open transparent umbrella from her side to above her head. The view cuts to <Subject 3>, where her reflection and the brightening sky ripple as her shoe passes along the puddle's edge.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance and clothing; show her from behind or rear three-quarter view first, then only her reflected silhouette and shoe. Do not reproduce the multi-view reference sheet.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Use the rainy sidewalk, warm lights and restrained early-dawn palette; adapt the location to the sidewalk near the bridge and avoid requiring the full rainbow in the reference.
<Subject 3> (appears in [Shot 2]): partially_preserved - Keep a small shallow puddle, paving texture and subdued reflections without copying the reference background.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey dawn, with PBR-like materials, clean surfaces and restrained warm reflections. Fine rain visibly falls throughout; the pavement is damp with only a few small shallow puddles. The streetlights are still on and the sky is beginning to brighten.
[Shot 1] From a low rear three-quarter angle on the sidewalk near the bridge, <Subject 1> walks beside a warm streetlamp in <Subject 2>. The transparent umbrella is already open and held low at her side. She steadily lifts the same open umbrella over her head, keeping her hand on its handle throughout. A few water beads fall from the canopy and briefly glint in the warm lamplight and faint early-dawn light; they remain small, natural drops. Rain continues visibly in the background, where a few wet hydrangeas and soft shop lights frame the street. She holds the umbrella naturally overhead once the movement is complete.
[Shot 2] At 00:06.500, cut to an extremely low view across <Subject 3>, a small shallow puddle near the same sidewalk. Its surface reflects <Subject 1>'s umbrella silhouette, a warm streetlamp and the gently brightening sky. Her shoe passes through the puddle's edge with a light step, sending a modest ripple across the water that softly breaks up the reflection. The surrounding paving remains visible. The camera tilts slightly upward with her movement, holding the rainy street atmosphere to the end.

overall_soundscape: Continuous distant city rain and traffic. As the raised umbrella catches rain, close umbrella patter returns; a light footstep and small splash are heard at the puddle. No dialogue or dramatic sound effect.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 13 秒的雨天黎明城市 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；湿润人行道、暖灯、紫阳花和灰蓝晨色参考图2；小水洼、地砖和水面反光参考图3。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–6.5秒：从天桥切到桥下人行道，低机位从背后或侧后方看洛天依。她走过仍亮着暖光的路灯，手中透明伞已经打开并放低在身侧；她平稳地把同一把伞举回头顶，始终握住伞柄。伞沿的几滴水随动作落下，在路灯暖光和微弱晨光里短暂闪亮。细雨持续落下，路边可见带水珠的紫阳花与柔和店灯。
2. 镜头2 6.5–13秒：切到极低机位的小水洼镜面。浅浅的水面映出她撑伞的轮廓、路灯余晖与渐渐亮起的天空，水洼周围仍能看见湿润地砖。她的鞋尖从水洼边缘轻踏经过，激起一圈小涟漪，轻轻打散倒影；镜头顺着她前行的方向微微上仰。

【音频风格】
远处城市雨声和车流声持续；伞回到头顶后，近处雨点重新落在伞面。鞋尖经过水洼时有轻微踩水声。无对白，不另作配乐。

【运镜与核心约束】
先以低位背面或侧后景表现完整举伞动作，再切到低机位水洼倒影。伞始终保持打开并握在手中；雨丝持续可见，水洼小而浅，水珠和反光克制。省略下天桥楼梯的过程。
```

## 剪辑与衔接

- 已检查 `output\shot35-36.mp4` 的尾帧：画面边缘可见洛天依灰色衣摆与发梢，前方为湿润天桥栏杆；伞不在该尾帧内。按 35–36 的剧本意图，新段以伞已打开、放低在身侧接起，但最终需结合选用的实际画面确认。
- 通过切镜从桥上到桥下人行道，以连续雨声、相近运动方向衔接；不要求两个地点在同一镜头里走通。
- 约第 6.5 秒从举伞切到水洼，最终对齐 3:37 和动作完成度；鞋尖只轻踏水洼边缘，呼应镜头 01 的涟漪，避免大面积积水。
- 如果模型不能稳定表现同一把打开的伞从身侧举到头顶，或倒影与鞋的关系不正确，可分别生成举伞、水洼倒影、鞋尖轻踏三个素材再剪接；伞与人物方向在不同素材间需核对。
- 水珠闪光以自然路灯反射为主，不需要额外粒子特效。38 结束后的轻微上仰可切到 39 的单一黎明城市远景，雨声保持连续。
