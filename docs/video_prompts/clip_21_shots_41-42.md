# 片段 21｜清晨上车与身旁的空座（剧本镜头 41–42）

- 成片区间为 3:56–4:08。横屏 16:9，建议生成 **13 秒**，取约 12 秒，留约 1 秒剪辑余量。
- 片内 0–6.5 秒是车外进站，6.5–13 秒是车内空座。以硬切省略跨门、走过车厢和落座的过程。42 开场时洛天依已经坐在靠窗位置。
- 从 40 的伞下侧脸切到清晨站台，沿用淡暖晨光与持续的细雨。三张图均为视觉参考。

## 参考图上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低马尾、花饰和灰色布料风衣。
2. **图2 / Picture 2 — C 组清晨站台**：`MV/pictures/C_anime_pbr/11_dawn_bus_stop.png`。参考蓝白公交、雨棚、路缘和清晨光线。调整车外机位，让车门对准站台可通行处。
3. **图3 / Picture 3 — C 组公交双人座**：`MV/pictures/C_anime_pbr/12_bus_interior_double_seat.png`。参考蓝色织物双人座、橙色扶手和挂着雨痕的侧窗。洛天依坐在靠窗的一侧，紧邻过道的座位整个保留在画面里。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi from <Picture 1>, with silver-grey hair in a low ponytail, a flower hair clip and a grey fabric trench coat. She carries a transparent umbrella.
<Subject 2> is the rainy morning bus stop and blue-and-white city bus in <Picture 2>.
<Subject 3> is the bus interior in <Picture 3>, with two adjacent forward-facing blue fabric seats, an orange handrail and a rain-streaked side window.

summary:
[reference generation] A bus pulls into <Subject 2> and <Subject 1> folds her umbrella at the stop. A hard cut finds her already seated by the window in <Subject 3>, with the seat next to her empty.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep her hairstyle, flower clip and grey coat. The same clear umbrella is open at the stop and folded beside her knees inside.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep the shelter and bus livery. Frame the passenger door beside a clear section of the curb.
<Subject 3> (appears in [Shot 2]): partially_preserved - Keep the blue double seat, orange rails and window. The aisle-side seat stays empty and fully visible.

detailed_description:
A semi-realistic Japanese anime film in soft grey-blue morning light with a little warm dawn color. Fine rain is visible on the street and against the bus windows.
[Shot 1] A steady medium-wide view of <Subject 2> from the sidewalk. The blue-and-white bus rolls slowly over the wet lane and stops parallel to the curb. Its passenger door opens at a clear boarding gap. <Subject 1> stays on the sidewalk and closes her wet transparent umbrella with one controlled motion. A passenger ahead moves through the doorway. She waits briefly, then takes a step toward the open door. End while she is still on the platform.
[Shot 2] At 00:06.500, hard cut inside the same bus. From across the aisle, frame <Subject 3> in a stable three-quarter medium view. <Subject 1> is already seated upright in the window-side seat, holding her folded umbrella upright beside her knees with the tip resting on the floor. The whole adjacent aisle-side seat, including its blue cushion and backrest, remains visible and empty. She quietly looks out the rain-streaked window. The bus doors close off-screen while she holds her gaze outside.

overall_soundscape: Soft rain, a low engine and tires crossing wet pavement at the stop. After the cut, a subdued door close and cabin hum, with rainfall muffled through the glass. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 13 秒的清晨公交 MV 片段。洛天依的外貌和灰色风衣参考图1。蓝白公交、候车雨棚和清晨光线参考图2。车内的蓝色双人座、橙色扶手和雨痕侧窗参考图3。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–6.5秒：清晨细雨中，从人行道一侧拍公交站中远景。蓝白公交沿湿路缓缓进站，贴着路缘停稳后打开车门，车门对着站台无遮挡的上车位置。洛天依在人行道上收拢透明伞，等前一位乘客上车，再朝车门迈出一步。镜头在她仍位于站台时结束。
2. 镜头2 6.5–13秒：直接切到同一辆公交的车内。机位在过道对面，三分之四侧角同时拍到双人座和雨窗。洛天依已经坐在靠窗一侧，手扶着立在膝边的湿伞，伞尖落在地板上。靠过道的蓝色座椅连同椅背和座垫完整可见，始终空着。她安静望向窗外，画外响起轻轻的关门声，镜头在这个构图上停留。

【音频风格】
车外有持续细雨、轮胎驶过湿路和轻微引擎声。切进车内后听见低沉的关门声和车厢声，窗外雨声隔着玻璃变柔。无对白，歌曲在后期接续。

【运镜与核心约束】
车外固定中远景接车内稳定中景。硬切省略人物经过车门、走过车厢和坐下的过程。车内保持清楚的双人座布局、靠窗的人和相邻的空位，折好的伞始终留在膝边。
```

## 剪辑衔接

- 已检查 Shot 40 的尾画面。洛天依撑开透明伞望向晨光，41 保持同一外出造型与透明伞。
- 剧本切点为 4:02。车内先建立空座和她望向窗外的状态，贴窗与转头朝前留给 43–44。
