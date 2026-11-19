# 片段 10｜站牌檐下：雨声先改变（剧本镜头 19–20）

## 片段信息

- 剧本成片区间：1:40–1:54；镜头 19 为 1:40–1:47，镜头 20 为 1:47–1:54。
- 建议设置：横屏 16:9，生成 **15 秒**，成片取约 14 秒，预留约 1 秒剪辑余量。建议 0:00–0:07.5 建立站牌和规律雨声，0:07.5–0:15 展示袖口、檐边水滴和握伞的手；实际按歌曲、动作和声音调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图用于人物和场景，不是固定首帧。前一片段末尾是城市仰景，此处通过切镜进入站牌。
- **声音顺序是叙事重点**：先建立规律的檐边滴答；她注意到湿袖口，准备调整伞；接着檐边滴答变稀疏、近处伞面雨声变薄，声音变化发生在她停下动作之前；再看到她握伞的手停住。远处城市雨声和歌曲持续，不静音。
- 生成声音可以作为素材参考，最终应在后期分层制作并试听，确保雨纹理真的先变化；不能仅靠角色表情表示雨声发生变化。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰、蓝眼睛和灰色布料风衣；多视图是同一人。
2. **图2 / Picture 2 — C 组公交站**：`MV/ab_test/C_anime_pbr/03_bus_shelter.png`。参考玻璃候车棚、屋檐、长椅、暖灯与雨夜城市；站牌文字不要求复现。

两个模型版本按相同顺序上传。洛天依独自站在站牌屋檐下，手持打开的透明伞；自然撑伞，不要求伞偏向某一侧。外景的雨始终可见，乐正绫及其他虚影不出现在本段。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory, blue eyes and an opaque grey fabric trench coat.
<Subject 2> is the rainy-night bus shelter from <Picture 2>, with a roof edge, glass panels, bench and warm lights against a blue-grey city.

summary:
[reference generation] <Subject 1> stands under <Subject 2>'s roof and watches the rain. Regular drops from the eaves become sparse and nearby umbrella rain thins before she stops a small movement of her umbrella handle.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 4]): partially_preserved - Keep one character's appearance and grey coat; use hand and sleeve close-ups where appropriate, without reproducing the reference-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 3]): partially_preserved - Keep the shelter roof, glass and rainy city atmosphere while changing to an eaves close-up.

detailed_description:
A semi-realistic Japanese anime rainy night, with PBR-like glass and metal, clean surfaces and restrained warm reflections. Fine rain falls visibly outside the shelter throughout; the pavement is wet with only small shallow puddles.
[Shot 1] A steady medium-wide view of <Subject 2>. <Subject 1> stands under the shelter roof with her open transparent umbrella, quietly watching the rain. Water drips from the nearby roof edge at a clear, regular pace. Umbrella patter is audible close by; distant city rain and traffic continue underneath. She holds the umbrella naturally above her, with no other person beside her.
[Shot 2] At 00:07.500, cut to a close view of <Subject 1>'s damp coat cuff and hand on the umbrella handle. She notices the wet fabric and begins a small movement to adjust her grip and umbrella. The roof drips are still regular at first.
[Shot 3] At 00:09.500, cut to a close view of the edge of <Subject 2>'s roof. The following drips become noticeably farther apart, with slightly longer tails; at the same time, nearby umbrella patter grows thinner. Distant rain and city traffic remain audible and the visible rain outside continues to fall. This sound change happens before her movement stops.
[Shot 4] At 00:12.000, cut back to <Subject 1>'s hand on the umbrella handle. Having begun the adjustment, her hand pauses mid-movement in response to the changed rain sound. Hold on the still hand while the sparse roof drips and thinner umbrella patter remain audible. Distant city rain continues through the end.

overall_soundscape: Layered continuous city rain and distant traffic; regular roof drips first, then distinctly sparser roof drips and thinner close umbrella rain before the hand stops. Do not silence the distant rain. No dialogue or musical sting.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 15 秒的雨夜公交站 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；玻璃候车棚、屋檐与雨夜城市参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–7.5秒：站牌屋檐下中远景。洛天依独自站着，手持打开的透明伞，安静看向雨中的街道。檐边水滴一颗接一颗规律落下；伞外能清楚看见雨丝，远处车流与城市雨声持续。
2. 镜头2 7.5–9.5秒：切到她的湿袖口与握伞的手。她注意到袖口沾湿，手开始轻轻移动，准备调整伞；此时檐边滴答仍然规律。
3. 镜头3 9.5–12秒：切到屋檐边缘近景。接下来的水滴由规律变得稀疏，滴水声尾音略长；与此同时，近处伞面雨声变薄。远处的雨声和车流声仍在，屋檐外的雨也继续向下落。
4. 镜头4 12–15秒：切回洛天依握伞柄的手。雨声变化已经发生，她调整到一半的手随之停住；镜头在静止的手上停留，稀疏滴答与变薄的近处雨声仍然可听见。

【音频风格】
先听见规律清晰的檐边滴答和近处伞面雨声，再听见檐边滴水变稀疏、伞面雨声变薄，随后她的动作才停住。远处城市雨声与车流声全程持续；无对白，不另作配乐。

【运镜与核心约束】
从站牌中远景切至湿袖口和伞柄，再切檐边水滴，最后切回握伞的手。洛天依自然撑伞；雨丝在屋檐外始终可见，地面湿润、只有局部小水洼。声音变化先于人物停下动作。
```

## 剪辑与衔接

- 已检查 `output\shot17-18rear.mp4` 的尾帧：高楼之间的雨夜仰景。此段从城市仰景切到站牌檐下，以远处城市雨声跨切镜衔接；未把该尾帧作为首帧。
- 19 先建立至少几次清楚、规律的滴答；20 中声音先变稀疏、变薄，再切回停住的手。不要依赖单纯静音或模型自动配音，后期应实际铺设并试听声音变化。
- 约第 7.5 秒进入袖口与伞柄，9.5 秒切檐边，12 秒切回握伞的手；最终对齐歌曲 1:47 及实际生成动作，预留约 1 秒剪辑余量。
- 若一次生成无法稳定完成袖口、滴水变化和手的反应，可拆成站牌、湿袖与伞柄、檐边滴水、手停住四个短镜头，再用分层雨声确定因果顺序。
- 结尾停在握伞的手，可在 21 接她抬头看向街道的反应；该段不提前出现乐正绫身影。
