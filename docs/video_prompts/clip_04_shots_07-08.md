# 片段 04｜檐边滴水与公交站（剧本镜头 07–08）

## 片段信息

- 剧本成片区间：0:25–0:37；镜头 07 为 0:25–0:31，镜头 08 为 0:31–0:37。
- 推荐页面设置：横屏 16:9，生成时长 **14 秒**。建议片段内 0:00–0:07 对应镜头 07，0:07–0:14 对应镜头 08；最终各取约 6 秒，约 2 秒供剪辑。实际切点以动作完成度和最终混音为准。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图用于人物和环境，不是固定首帧。镜头 07 中从手部切到站牌附近水洼；镜头 08 再切为站牌中远景。
- 歌曲在后期作为全片连续主音轨；檐边滴水、雨声和公交车声可后期分别铺设。无对白，不另作音乐。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考同一人的银灰色低位马尾、头顶发环、花饰与灰色布料风衣；不把设定图布局或多个视角生成为多个人。
2. **图2 / Picture 2 — 便利店街道**：`MV/ab_test/C_anime_pbr/02_convenience.png`。用于镜头 07 的街边屋檐及暖冷光关系；按近景需要调整视角。
3. **图3 / Picture 3 — 公交站**：`MV/ab_test/C_anime_pbr/03_bus_shelter.png`。用于站牌附近水洼和公交站候车棚、长椅、雨夜城市环境；公交车由模型生成。

两个版本使用相同上传顺序。图中站牌文字不要求复制；伞延续前一段的透明伞，但近景按构图需要局部入画即可。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, crown hair loops, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy convenience-store street in <Picture 2>, providing the street-side eaves and warm storefront light.
<Subject 3> is the rainy bus shelter and its surrounding pavement in <Picture 3>, including the glass shelter, bench and city setting.

summary:
[reference generation] Under the eaves at <Subject 2>, <Subject 1> catches dripping rain in her hand; the view cuts to a small puddle near <Subject 3>, then to her seated at the bus stop as a bus arrives and leaves without her boarding.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 3]): partially_preserved - Keep one character and her outfit; the first shot shows only her hand and coat sleeve, not the character-sheet layout.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep the rainy street-side eaves and warm light, changing to a close view.
<Subject 3> (appears in [Shot 2], [Shot 3]): partially_preserved - Keep the bus-shelter environment and bench; use a close view of nearby paving and add a bus for the wide view.

detailed_description:
A semi-realistic Japanese anime city at rainy blue hour, with PBR-like materials, clean surfaces, soft warm lights and small shallow puddles. Rain visibly falls throughout: fine streaks descend outside the shelter, drops strike wet surfaces, and water drips from the eaves. Wetness is localized rather than flooding the street.
[Shot 1] Close view under the street-side eaves of <Subject 2>. <Subject 1>'s grey coat sleeve enters the frame as she extends one hand, palm up, into a thin stream dripping from the edge of the roof. Drops land in her palm and water runs naturally over her fingertips. Visible rain continues beyond her hand. Hold the small gesture long enough to read clearly.
[Shot 2] At 00:04.000, cut on the falling water to a close view of a small shallow puddle on the pavement near <Subject 3>. One drop strikes the water and spreads rings across a warm reflection; individual wet paving stones remain visible around it. Fine rain keeps falling.
[Shot 3] At 00:07.000, cut to a medium-wide view of <Subject 3>. <Subject 1> is already seated at one end of the bench; the place beside her is visibly empty. A bus pulls in along the roadway in front of the stop, pauses, and then drives away. She briefly looks up at it and remains seated; she does not board. The empty place stays empty. Rain remains clearly visible against the dark city and illuminated shelter throughout the shot, with droplets on the shelter glass and roof. Hold briefly as the bus leaves.

overall_soundscape: Continuous rain and distant traffic. Distinct roof drips and water on skin in the opening, followed by a soft puddle impact; bus tires pass over the wet road, then the rain becomes clear again. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜屋檐和公交站的 MV 片段。洛天依的外貌、低位马尾、花饰和灰色布料风衣参考图1；图中多个视角为同一个人。街边屋檐和便利店附近的暖光参考图2；公交站候车棚、长椅与周围城市参考图3。采用半写实二次元、PBR 质感，两个场景中都能看见持续降雨。

【情节概要】
1. 镜头07：屋檐下手与雨水近景。洛天依伸手接屋檐滴水，水线从指尖滑落；顺着水滴切到公交站附近的小水洼，雨滴落下形成涟漪。
2. 镜头08：切到公交站中远景。她坐在长椅一侧，身旁座位空着；公交车进站又离开，她抬头看一眼，留在原处，没有上车。

【音频风格】
雨声和远处城市声连续；屋檐滴水在近景更清晰，车轮掠过湿路后，雨声重新清晰。无对白，不另作配乐，歌曲后期与全片主音轨对齐。

【运镜与核心约束】
从手部近景切到水洼，再切至公交站中远景。雨丝持续可见，雨滴落在手、地面和候车棚上；地面只有局部小水洼。候车时身旁空位始终没有人。
```

## 剪辑与衔接

- 已检查 `output\clip05-06.mp4` 的末尾画面：洛天依位于便利店橱窗外，手持透明伞。07 从屋檐下的手部近景切入，可通过雨声跨镜衔接；不需要把原视频尾帧当作固定首帧。实际成片选择的尾帧仍可能不同。
- 07 约第 4 秒从手切到公交站附近水洼，约第 7 秒切到 08；最终按剧本各保留约 6 秒，并对齐歌曲。
- 车进站、停靠、离站及她抬头的动作在一段短镜头中可能难以稳定完成。若生成不理想，可分别生成候车、公交驶入或驶离的素材，再通过切镜与车声完成动作；保持她坐在原处和空座连续。
- 08 结尾她仍坐在站台，为 09 的起身和玻璃倒影留出衔接空间；具体方向以实际生成结果为准。
