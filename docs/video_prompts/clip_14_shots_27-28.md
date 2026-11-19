# 片段 14｜走上横跨道路的天桥（剧本镜头 27–28）

## 片段信息

- 剧本成片区间：2:28–2:40；镜头 27 为 2:28–2:34，镜头 28 为 2:34–2:40。
- 建议设置：横屏 16:9，生成 **13 秒**；成片取约 12 秒，预留约 1 秒剪辑余量。建议片内 0:00–0:06.5 是背后低位上楼梯，0:06.5–0:13 是天桥与城市远景；实际切点按动作及歌曲调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片提供人物与桥的场景参考，不是固定首帧。
- 前段山坡观景台与本段市区天桥不是紧邻地点。以栏杆滴水、车灯或雨声切镜省略下山路程，不要求人物在一镜内走完全程。
- 本段洛天依自然撑透明伞，雨丝持续可见；**镜头 27–28 桥上没有乐正绫或其他虚影**。她的身影要到镜头 29 才淡入。
- 歌曲后期连续对齐；楼梯脚步与桥下车流可稍突出，进入城市远景时车流变远，雨幕变开阔。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰和灰色布料风衣；多视图是同一人。
2. **图2 / Picture 2 — C 组天桥外景**：`MV/pictures/C_anime_pbr/08_bridge_exterior.png`。参考道路两侧的楼梯、桥面、栏杆、车流和雨夜城市；人行桥面位于道路上方，车辆从桥下行驶。参考图的桥体与楼梯连接仍需在生成后核对。

两个版本按相同顺序上传。桥面是横跨公路的人行通道，楼梯连接两侧人行道；车与行人处于上下不同层级。**不用先前不合格的桥面视角候选图作为参考。**

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy-night pedestrian overpass from <Picture 2>: a raised walkway crossing above a roadway, connected to sidewalks by stairs at the ends, with city traffic below.

summary:
[reference generation] <Subject 1> climbs the near staircase of <Subject 2> with a transparent umbrella, then appears on the raised walkway in a wide city view while cars pass on the road underneath.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance and grey coat; show her from behind on the stairs, then as a small figure on the bridge. Do not reproduce the character-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the same stairs, railings, elevated pedestrian deck and rainy city; adjust camera views while maintaining a clear crossing above the road.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like glass and metal, clean surfaces and restrained warm and neon reflections. Fine rain visibly falls throughout. Pavements are damp with only small shallow puddles.
[Shot 1] A low rear view follows <Subject 1> as she climbs the near staircase of <Subject 2>. She wears a grey coat and holds her open transparent umbrella naturally overhead; the umbrella partly masks the rainy sky. Her feet rise along the wet steps toward the elevated pedestrian deck, with a continuous handrail beside the stairs. Rain strikes the steps and canopy; road traffic is below and beside the staircase. No apparition is on the stairs or bridge.
[Shot 2] At 00:06.500, cut to an exterior wide view of the same <Subject 2> and its surrounding city. The pedestrian deck runs across and clearly above the road; cars travel on the road beneath it, and the staircases connect the elevated deck to sidewalks on the two sides. High-rises, city lights and a raised railway provide depth behind the bridge. <Subject 1> is a small figure on the pedestrian deck, walking a few steps and coming to a stop. Keep pedestrians on the bridge and cars below, with the crossing unmistakable. Rain remains visible against the darker city and bridge lighting. Hold the wide view through the end; no other figure or apparition appears on the bridge.

overall_soundscape: Continuous rain and city traffic. Footsteps on wet stairs and road traffic beneath the bridge are clear in the first shot; in the wide view the traffic sounds farther away beneath an open rain ambience. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 13 秒的雨夜人行天桥 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；天桥楼梯、横跨道路的桥面、栏杆与雨夜都市参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–6.5秒：从洛天依背后低位跟拍。她身穿灰色风衣，自然撑着透明伞，沿近侧人行道的湿润楼梯一步步走上天桥；伞面遮住一部分雨夜天空。雨落在伞面与台阶上，桥下和楼梯旁有道路车流。
2. 镜头2 6.5–13秒：切到同一座天桥及城市的宏伟远景。人行桥面从公路一侧横跨到另一侧，高于公路；车辆在桥下的道路上行驶，两端楼梯通向人行道。高楼、城市灯光与高架铁路在远处形成层次。洛天依是桥面上的小小身影，她向前走几步后停住；雨继续落下。

【音频风格】
雨声和城市车流声持续。第一镜中湿台阶脚步与桥下车辆声较清楚；切至远景后车流听起来更远，雨幕更加开阔。无对白，不另作配乐。

【运镜与核心约束】
先从背后低位跟随上楼，再切到同一座天桥的外部远景。桥面必须跨越道路并在车辆上方，楼梯连接道路两侧的人行道，车辆只在桥下道路行驶。雨丝持续可见，地面湿润，只有局部小水洼；本段桥上只有洛天依，不出现乐正绫或其他虚影。
```

## 剪辑与衔接

- 已检查 `output\shot25-26.mp4` 的尾帧：雨珠停留在山坡观景台的栏杆上，远处城市灯光虚化。可以用滴水声或相似的城市灯光切至天桥楼梯，省略下山与返回市区的路程；不是同一地点的连续走路。
- 约第 6.5 秒切到天桥外景，最终按 2:34 的歌曲切点与可用动作调整。上楼特写与外景若难在一次生成中保持一致，可分别生成并在剪辑中接合。
- C 组 `08_bridge_exterior.png` 的桥体看起来横跨车道，但楼梯与桥面的连接仍应逐处复核；以前的桥面视角候选图存在道路方向或楼梯问题，不应当成已通过的几何参考。
- 生成后检查近端楼梯是否从人行道通到桥面、远端楼梯是否落在人行道、车辆是否在桥下，以及洛天依是否确实停在桥面上。无法同时满足时，分别制作楼梯近景和桥外景，避免把有误结构作为连续空间使用。
- 本段以洛天依独自停在桥上结束，镜头 29 的乐正绫身影才在前方雨雾中柔和淡入。
