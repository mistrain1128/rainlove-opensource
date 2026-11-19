# 片段 09｜伞下的空位与雨夜城市（剧本镜头 17–18）

## 片段信息

- 剧本成片区间：1:27–1:40；镜头 17 为 1:27–1:34，镜头 18 为 1:34–1:40。
- 建议设置：横屏 16:9，生成 **14 秒**；成片取约 13 秒，预留约 1 秒剪辑余量。建议片内 0:00–0:07.5 对应伞下伸手，0:07.5–0:14 对应雨滴落地和城市仰拍；实际切点按歌曲和画面调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片用于人物和场景参考，不是固定首帧。
- 雨声是叙事线：靠近悬浮水滴时，近处伞面雨声略变薄，远处城市雨声和歌曲保持；镜头 18 仍能听到远处雨声和近处滴水。建议后期分层处理。
- 本段不出现乐正绫或其他虚影；洛天依独自撑伞。音乐后期连续对齐，不生成对白或新配乐。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰发色、低位马尾、花饰和灰色布料风衣；多视图是同一个人。
2. **图2 / Picture 2 — C 组雨夜城市**：`MV/ab_test/C_anime_pbr/01_station_city.png`。参考雨夜日本都市、高楼、暖色灯光与半写实二次元材质；18 改为从街道向上仰拍，不要求照搬原图构图。

两个版本按相同顺序上传。透明伞、手和雨滴由提示词描述；图中建筑标识和文字无需复现。水迹局部存在，只有小浅水洼。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy Japanese city referenced from <Picture 2>, including blue-grey night, high-rise buildings and warm city lights.

summary:
[reference generation] Beneath her transparent umbrella in <Subject 2>, <Subject 1> reaches toward the empty space beside her and passes her hand through a few suspended raindrops. Water falls from her fingertips; the view tilts upward into the rainy city, where a few droplets rise against the falling rain.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's hairstyle and grey coat; in the second shot show only her hand before the camera moves upward. Do not reproduce the reference-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the rainy Japanese city, high-rises and warm lighting while adapting the framing to an umbrella close-up and a low-angle city view.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like materials, clean surfaces and restrained warm reflections. Rain streaks remain clearly visible throughout the exterior views; the ground has only small shallow puddles.
[Shot 1] Close view beneath <Subject 1>'s open transparent umbrella in <Subject 2>. She is in her grey coat; she holds the umbrella naturally above her. She slowly reaches one hand to her side and passes her fingers through a few raindrops suspended briefly in the air. Her hand and the small suspended drops are clear against the darker street, while normal rain continues falling outside the umbrella. There is no person in the empty space. Keep the gesture quiet and allow a moment for it to read.
[Shot 2] At 00:07.500, cut closer to <Subject 1>'s hand. A few drops slide from her fingertips and fall to the wet pavement, making small ripples in a shallow puddle. The camera then tilts up from the street toward the high-rise buildings and rain-lit sky of <Subject 2>, revealing a broad low-angle city view. A few isolated droplets rise slowly among the surrounding rain, while most rain continues falling normally. Warm lights glimmer through the rain; no figure or apparition appears. Hold briefly on the city view through the end.

overall_soundscape: Distant city rain and traffic continue throughout. The close umbrella-rain texture thins slightly while the hand passes through the suspended drops, without becoming silent; soft drops fall near the end. No dialogue or dramatic effect sound.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 14 秒的雨夜伞下与城市仰拍 MV 片段。洛天依的外貌、发型与灰色风衣参考图1；日本动漫都市的高楼、雨夜色调和灯光参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–4秒：洛天依撑着透明伞站在雨夜街道上，近景里，她慢慢把手伸向身旁，手指从几颗短暂停在空中的雨滴之间穿过；她身旁没有其他人。
2. 镜头2 4–7.5秒：细雨在伞外持续向下落。她的手经过悬浮雨滴时动作轻柔，雨滴与手在深色街景前清楚可见；镜头停留片刻，让这一动作完整呈现。
3. 镜头3 7.5–11秒：切近她的手，几滴水从指缝滑下，落到湿润地面的小水洼中，泛起细小涟漪。镜头随即从街道向上抬起，望向高楼和雨幕中的夜空。
4. 镜头4 11–14秒：城市仰拍里，远处暖色灯光穿过雨幕；少量水滴缓慢向上升起，周围大部分雨仍向下落。画面停留在雨夜城市，不出现乐正绫身影或其他虚影。

【音频风格】
远处城市雨声与车流声持续；手穿过悬浮雨滴时，近处伞面雨声略微变薄但不静音，随后听见细微滴水。无对白，不另作配乐。

【运镜与核心约束】
从伞下手部近景切到指缝滴水，再由地面向上仰拍高楼。洛天依独自撑伞；雨丝始终可见，只有少量水滴逆向升起。湿地只保留局部小水洼与克制反光。
```

## 剪辑与衔接

- 已检查 `output\shot15-16.mp4` 尾帧：白天家中，洛天依和乐正绫坐在雨窗旁。17 直接切回雨夜伞下，先让窗雨声延续、再融入伞面雨声；不是同一时空的连续机位，也不使用该尾帧作为雨夜首帧。
- 17 中伸手穿过的是少量短暂停留的雨滴；18 中几滴水从指缝落地后，城市视野中另有少量雨滴向上升起。周围大部分雨始终向下落，避免整场雨反转。
- 约第 7.5 秒进入指缝滴水，最终按 1:34 唱句和动作调整。若手、悬浮水滴及仰拍在一次生成中不稳定，可分别生成伞下伸手和滴水转城市，再后期组接。
- 18 保持无人影的城市景观，结尾为接续 19 的站牌檐下看雨留空间；19 的屋檐滴水节奏和 20 的雨声变化需在后续单独设计。
