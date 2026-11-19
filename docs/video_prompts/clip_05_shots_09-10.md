# 片段 05｜雨夜倒影与逆向水纹（剧本镜头 09–10）

## 片段信息

- 剧本成片区间：0:37–0:50；镜头 09 为 0:37–0:43，镜头 10 为 0:43–0:50。
- 推荐页面设置：横屏 16:9，生成时长 **15 秒**。建议片段内 0:00–0:07 对应镜头 09，0:07–0:15 对应镜头 10；最终分别取约 6 秒和 7 秒，约 2 秒留给剪辑。实际切点以动作和最终混音为准。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片用于人物、场景及水洼质感参考，不是固定首帧。
- 主歌曲后期连续对齐；此片段以雨声、街道环境声和水滴声为主，不生成对白或新配乐。10 的演唱为剧本可选项，本版先使用闭口表演，避免与最终主唱口型冲突。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考角色容貌、银灰色低位马尾、头顶发环、花饰和灰色布料风衣。多视图共同代表同一个人。
2. **图2 / Picture 2 — C 组公交站**：`MV/ab_test/C_anime_pbr/03_bus_shelter.png`。参考站台长椅、湿玻璃和雨夜城市；09 从站台起身并经过玻璃。
3. **图3 / Picture 3 — C 组小水洼**：`MV/ab_test/C_anime_pbr/04_puddle.png`。仅参考局部浅水洼、地砖与灯光倒影；将其放在公交站附近，不把图中的车站建筑强制带入画面。

两个版本按同一顺序上传。本片段不使用乐正绫参考图、不出现虚影；原有虚影片段由后期剪掉，普通玻璃倒影或雨景可按素材需要选用。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, crown hair loops, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy bus shelter in <Picture 2>, including its bench, glass panels and surrounding city street.
<Subject 3> is the small shallow puddle and wet paving referenced from <Picture 3>; its texture and reflected lights are transferred to the pavement near the bus stop.

summary:
[reference generation] At <Subject 2>, <Subject 1> rises and passes rain-streaked glass, seeing her own reflection and the city lights. She lowers her gaze, and a raindrop falls into <Subject 3>, whose ripples briefly draw inward.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance and clothing; do not reproduce the reference sheet's layout or multiple views.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the bus-shelter bench, wet glass and rainy city atmosphere while changing viewpoint.
<Subject 3> (appears in [Shot 3]): partially_preserved - Keep a small puddle, paving and restrained reflections, relocating them near the bus shelter rather than reproducing the background architecture.

detailed_description:
A semi-realistic Japanese anime city at rainy blue hour, with PBR-like glass and metal, restrained warm reflections and clean surfaces. Fine rain streaks visibly descend in front of the shelter and in the background throughout; drops gather and run down the glass. Only small shallow puddles interrupt the wet paving.
[Shot 1] At <Subject 2>, <Subject 1> rises from the bench and passes alongside the rain-streaked glass. Only her own reflection and the city lights appear on the glass. Rain falls visibly beyond the shelter; ordinary passersby move along the wet street. Keep the gesture quiet and natural.
[Shot 2] At 00:07.000, cut to a close view of <Subject 1>'s face near the same shelter. Rain remains visible outside behind her. She lowers her eyes gently, lips closed, and the camera holds her thoughtful expression for a moment.
[Shot 3] At 00:11.000, cut to <Subject 3>, a small shallow puddle on the pavement near the shelter. A raindrop falls into it. The ripple rings briefly draw inward toward the point of impact, a subtle moment of reversed motion, while surrounding rain continues to fall normally. The reflected city lights shift gently and the rain continues through the end.

overall_soundscape: Continuous rainfall and distant city traffic throughout; nearby drops become slightly clearer in the final close-up. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜公交站及附近水洼的 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；公交候车棚、长椅与湿玻璃参考图2；小水洼、湿地砖和灯光倒影参考图3，水洼位于公交站附近。采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头09：洛天依从站台长椅起身，经过湿玻璃；玻璃只映出她自己与街灯。
2. 镜头10：切到洛天依脸部近景，她轻轻低下视线；再切到地上的小水洼，雨滴落下后，水纹短暂向中心收拢，周围雨滴仍正常下落。

【音频风格】
雨声和远处城市声持续，近处水滴在水洼近景逐渐清晰。无对白，不另作配乐。

【运镜与核心约束】
由站台湿玻璃倒影切至脸部近景，再切至水洼特写。雨丝始终清晰可见，玻璃上有向下流动的雨痕；水洼小而浅，反光克制。本片段不出现乐正绫虚影。
```

## 剪辑与衔接

- 已检查 `output\shot08_1114_225215.mp4` 末尾：洛天依坐在站台，公交车已驶近。该片段没有确认车辆离站，若成片需要保留 08 的“车离开”，应补充离站素材或以车声和切镜交代，再接 09 起身；不要把离站当作已生成。
- 原有虚影段落后期剪掉；09 的普通玻璃倒影可选用，也可用雨景替代。之后的乐正绫雨中身影采用朦胧雾感和柔和淡入、淡出。
- 10 的逆向水纹只持续一瞬，其余雨仍向下落；可单独生成水洼特写，或后期局部处理，避免模型将整场雨反转。
- 约第 7 秒切脸部近景，约第 11 秒切水洼；最终对齐 0:43 和歌曲进入副歌的位置。结尾雨声、雨滴动作可引入 11 的伞沿微距。
