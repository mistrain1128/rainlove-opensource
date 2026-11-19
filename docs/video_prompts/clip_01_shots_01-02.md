# 片段 01｜水洼与雨夜车站（剧本镜头 01–02）

## 片段信息

- 剧本区间：0:00–0:08；片段内 0:00–0:04 对应镜头 01，0:04–0:08 对应镜头 02。
- 推荐页面设置：横屏 16:9，时长 8 秒。实际剪辑点以最终洛天依混音校准。
- 模式：MiniMax H3 使用多图参考 Ref2VA；Wan 3.0 使用多图参考。图片是视觉参考，不要求把任何一张当作固定首帧。
- 配乐：以最终确认的歌曲为整支 MV 的主音轨，后期从歌曲开头对齐；此片段不让模型另作音乐。环境雨声可生成或后期单独铺设。最终混音版本尚未在本提示文件中锁定。
- 标题：片名及水纹显隐在后期添加。当前片名《雨还在下》为故事暂定名称，本片段生成画面先不写字。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 小水洼质感**：`MV/ab_test/C_anime_pbr/04_puddle.png`。只借用局部小浅水洼、湿地砖、克制反光和雨夜配色；图中的周边环境不作为镜头 01 的实际地点，水洼应位于车站附近。
2. **图2 / Picture 2 — 车站与城市**：`MV/ab_test/C_anime_pbr/01_station_city.png`。参考车站入口、广场、高架铁路、灯光与半写实二次元城市氛围；镜头 02 按剧本改为更高机位，不要求复制该图的低机位构图。图中文字和标识不作为必须复现的内容。
3. **图3 / Picture 3 — 洛天依造型**：`MV/pictures/Luo Tianyi.png`。仅参考同一个人的银灰单马尾、花饰与灰色布料风衣造型；镜头 02 中她只是在车站屋檐下的一个小小身影。不要把设定图的多视角或四宫格当作画面内容。

图片以该顺序上传；以下模型正文内的图号和素材对应关系以此为准。

---

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is the small, shallow puddle and wet pavement texture referenced from <Picture 1>; its size, restrained ripples and warm reflections are used, while the surroundings in the image are not the target location.
<Subject 2> is the rainy-night station plaza referenced from <Picture 2>, including its station entrance, elevated railway, amber station lights and blue-grey city atmosphere.
<Subject 3> is Luo Tianyi, one person, referenced from <Picture 3> for her silver-grey side ponytail, flower hair accessory and opaque light-grey fabric trench coat.

summary:
[reference generation] Create the opening two-shot sequence around <Subject 1>, <Subject 2> and <Subject 3>, moving from a small puddle near the station to a high, wide view of the station and its surrounding city.

retention_analysis:
<Subject 1> (appears in [Shot 1]): partially_preserved - Keep the small puddle, wet paving and restrained reflections; place them near the station rather than at the pictured shop.
<Subject 2> (appears in [Shot 2]): partially_preserved - Keep the station, elevated railway and lighting as environmental references while changing the camera to a higher, wider viewpoint.
<Subject 3> (appears in [Shot 2]): partially_preserved - Use the character design for one distant figure beneath the station awning; do not reproduce the reference sheet layout.

detailed_description:
A semi-realistic Japanese animated-film style, with PBR-like materials, rainy blue-grey night, warm station lights and clean, restrained surface detail. [Shot 1] A fixed close-up frames <Subject 1>, a small shallow puddle among visible paving stones near the station. Raindrops fall into the puddle and create overlapping rings; reflected station lights bend and break gently in the ripples. The surrounding ground remains visible and wet rather than flooded. [Shot 2] At 00:04.000, the camera cuts to a high, wide view of <Subject 2>: the illuminated station entrance, bus lanes, elevated railway and layers of city windows recede into the rainy night. <Subject 3>, a single very small figure in a grey coat with a silver-grey ponytail, stands beneath the station entrance awning. The distant scale is maintained as the rain falls and distant traffic moves through the city. The camera holds the wide view until the end.

overall_soundscape: Nearby raindrops tap the pavement and puddle; distant traffic and the broader sound of rain continue through the cut. No spoken dialogue.

non_diegetic_music: N/A
```

---

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段半写实二次元、带有 PBR 质感的都市雨夜 MV 开场。参考图1中小水洼、地面水迹和克制的灯光反射；参考图2中的车站入口、广场、高架铁路和雨夜城市氛围；洛天依的银灰色单马尾、花饰与灰色风衣造型参考图3。图1中的周边环境不作为本片段地点；图3中的多个视角共同指向同一个人，不把角色设定表作为画面。

【情节概要】
1. 镜头01 0:00–0:04：车站附近一处局部浅水洼的固定特写。雨滴落入水中形成涟漪，倒映的车站灯光随水纹扭曲。水洼周围仍能看见湿润地面。
2. 镜头02 0:04–0:08：切到城市及车站高位远景。雨雾中的楼窗、道路、高架铁路和车站入口共同入画；洛天依是车站屋檐下一个小小身影。画面保持至片段结束。

【音频风格】
近处雨滴、水洼与远处交通雨声贯穿切镜，无对白。整首歌曲作为 MV 的主音轨在后期从开头对齐，本片段不另作配乐。

【运镜与核心约束】
镜头01为固定水洼特写；镜头02切至高位城市远景并保持。小水洼和水渍局部存在，保留雨夜城市的克制反光与动画背景质感。片名从水纹中浮现再淡去的文字效果留到后期添加。
```

## 剪辑与衔接

- 片名在镜头 01 的水纹区域后期叠加、随涟漪淡去；精确视觉形式留给剪辑阶段。
- 雨声和歌曲跨镜头连续，雨声保持近景水滴与远处城市雨幕的层次。
- 下一片段为下方镜头 03–04。两个片段之间按剧本切镜；实际生成后检查 02 的尾帧以及 03 的人物位置、出站方向和光线，再确定最终剪辑点。
- 如平台不能在一次生成中稳定完成两个场景切镜，可将镜头 01、02 分别生成并在后期按 0:04 切开；此做法需分别制作并选择各镜头的首帧。

---

# 片段 02｜车站：留给谁的位置（剧本镜头 03–04）

## 片段信息

- 剧本成片区间：0:08–0:15，镜头 03 为 0:08–0:12，镜头 04 为 0:12–0:15。
- 推荐页面设置：横屏 16:9，生成时长 **9 秒**。片段内建议 0:00–0:05 为镜头 03，0:05–0:09 为镜头 04；成片目标约 7 秒，约 2 秒为剪辑余量。切点和取舍根据生成结果调整，不改变歌曲时间轴。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图用于人物和环境，不是固定首帧。片段 01 实际尾帧尚未确定，先按切镜衔接，不能保证帧级连续。
- 配乐：歌曲后期对齐并贯穿。生成伞面和雨声供选用，最终也可后期单独铺设；不生成新的背景音乐或对白。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo Tianyi.png`。参考银灰色单侧马尾、蓝色眼睛、花饰和不透明灰色布料风衣；设定图中的多个视角为同一个人，不把版面或多个人物带入画面。
2. **图2 / Picture 2 — C 组车站**：`MV/ab_test/C_anime_pbr/01_station_city.png`。参考车站入口、玻璃雨棚、暖光、广场、高架铁路与半写实二次元材质；改变机位以服务动作。站名和标识不要求复现。

两个提示词版本都按此顺序上传，图号不要互换。行人由提示词描述，不以角色设定图生成多名洛天依。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person whose appearance and clothing come from <Picture 1>: silver-grey side ponytail, blue eyes, flower hair accessory and an opaque light-grey fabric trench coat.
<Subject 2> is the rainy station entrance and plaza from <Picture 2>, with its glass canopy, warm entrance lights, wet paving, elevated railway and blue-grey city atmosphere.

summary:
[reference generation] At <Subject 2>, <Subject 1> pauses as departing passengers leave, opens a transparent umbrella, and walks toward the street with the umbrella tilted over an empty space beside her.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance, hairstyle and fabric coat; do not reproduce the multiple views or layout of the reference sheet.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the entrance, canopy, station lighting and urban atmosphere while changing viewpoints to follow the action; exact signs are not essential.

detailed_description:
A semi-realistic Japanese anime city at rainy blue hour, with PBR-like glass and metal, clean surfaces, restrained reflections, wet pavement and only small shallow puddles. Warm station light falls against the cool rain outside.
[Shot 1] A medium-close view under the canopy of <Subject 2> shows <Subject 1> near the station entrance, holding a closed transparent umbrella. Ordinary passengers with umbrellas move away from the entrance and pass into the rain. She remains still for a brief moment, glancing toward the empty space beside her as if letting someone go first. No companion appears. She opens her umbrella completely and holds it steady as fine rain begins to tap its clear canopy. Keep the action gentle and legible, with a natural pause rather than exaggerated acting.
[Shot 2] At 00:05.000, cut to a medium rear view behind <Subject 1>, facing from the same station entrance toward the street. Her umbrella is fully open. She shifts its canopy toward the empty space on one side, leaving her own opposite shoulder exposed to the rain, and walks away from the canopy toward the street. A slow camera follows behind her. The empty space beneath the umbrella remains visibly unoccupied; the grey coat, side ponytail and flower accessory remain consistent. Let her continue walking for a moment before the clip ends, leaving an editable tail.

overall_soundscape: Continuous rain and distant station traffic. The umbrella opens with a soft mechanical rustle, followed by raindrops tapping the canopy; nearby footsteps remain subdued. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜车站的 MV 片段。洛天依的外貌、银灰色单侧马尾、花饰与灰色布料风衣参考图1；图1的多个视角共同指向同一个人。车站入口、玻璃雨棚、暖光、广场与高架铁路参考图2。画面采用半写实二次元和 PBR 质感。

【情节概要】
1. 镜头01：站口中近景。撑伞的人群离开，洛天依在屋檐下停顿，看向身旁空位，仿佛等身边的人先走；随后打开透明伞。
2. 镜头02：切到同一车站的背影跟拍。她将打开的伞偏向身边空着的一侧，自己的另一侧肩膀露在雨里，然后走向街道；伞下空位始终没有人物。

【音频风格】
雨声与远处交通声连续，伞打开时有轻微声响，雨点随后落在伞面上；无对白，不另作音乐。歌曲后期与全片主音轨对齐。

【运镜与核心约束】
先用站口中近景表现停顿和开伞，再切至背影缓慢跟拍。地面湿润，只有局部小水洼，反光克制；人物与场景造型在两个镜头间保持一致。
```

## 剪辑与衔接

- 生成片段约在第 5 秒切到背影；最终从两镜各自挑选可用时段，剪成剧本中的约 4 秒与 3 秒，实际切点随动作完成度及最终混音校准。
- 与 01–02 之间采用高位远景切到站口中近景；实际生成后再核对人物位置和行进方向，不把尚不存在的尾帧当作已确认参考。
- 片段结束时保持向街道行走，供后续镜头 05 的人行道跟拍衔接；生成后根据真实尾帧确认方向及伞偏向。
- 如果模型无法稳定完成开伞后切镜，分别生成镜头 03 和 04，再保证透明伞的打开状态、偏向及人物方向一致后剪辑。
