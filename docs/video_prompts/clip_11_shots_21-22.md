# 片段 11｜望向雨夜，走出屋檐（剧本镜头 21–22）

## 片段信息

- 剧本成片区间：1:54–2:04；镜头 21 为 1:54–2:00，镜头 22 为 2:00–2:04。
- 建议设置：横屏 16:9，生成 **11 秒**；成片取约 10 秒，留约 1 秒剪辑余量。建议片内 0:00–0:06.5 对应抬头及街道远景，0:06.5–0:11 对应走出屋檐；实际根据动作与歌曲调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图限定人物和场景，不是固定首帧。
- 上一片段近处雨声已经变薄；本段开头远处雨和车流持续，近处保持轻薄。她走出屋檐时雨点重新落在伞面，近处伞面雨声恢复。歌曲作为连续主音轨后期对齐；雨声建议后期分层制作。
- 本段不出现乐正绫身影。自然撑伞，不要求伞偏向空位。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰、蓝眼睛和灰色布料风衣；图中的多视图是同一人。
2. **图2 / Picture 2 — C 组公交站**：`MV/ab_test/C_anime_pbr/03_bus_shelter.png`。参考站牌屋檐、玻璃候车棚、暖灯、道路与雨夜城市；街道主观远景调整机位，远处山坡仅作为雨雾中模糊的背景。

两个版本按相同顺序上传。透明伞由提示词描述；图中站牌文字不要求复现。雨丝持续可见，地面湿润并只有局部小水洼。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory, blue eyes and an opaque grey fabric trench coat.
<Subject 2> is the rainy-night bus shelter and city street from <Picture 2>, with a roof, glass panels, warm streetlights and wet pavement.

summary:
[reference generation] After pausing under <Subject 2>, <Subject 1> raises her gaze toward the rainy street. She then walks out from under the shelter with her transparent umbrella, and the nearby umbrella-rain sound returns.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 3]): partially_preserved - Keep one character's appearance and grey coat, without reproducing the reference sheet's multiple views.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): partially_preserved - Keep the shelter, rainy street and warm lights while changing camera angles; a faint distant hillside may be seen through the rain.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like glass and metal, clean surfaces and restrained warm reflections. Fine rain visibly falls outside the shelter throughout. The pavement is wet, with only small shallow puddles.
[Shot 1] Under the roof of <Subject 2>, a close view begins near <Subject 1>'s hand holding the transparent umbrella handle after her movement has paused. She gently lifts her head and looks toward the street. Nearby umbrella patter and roof drips remain thin; distant city rain and traffic continue.
[Shot 2] At 00:02.000, cut to her point of view along the street: warm lamps shine through visible rain, a few vehicles pass, and a faint hillside is barely discernible beyond the city in the rain haze. No apparition appears. Hold the view for a quiet moment as the distant rain continues.
[Shot 3] At 00:06.500, cut to a rear medium view of <Subject 1> at the same shelter. Already standing, she holds her open transparent umbrella naturally and walks out from under the roof toward the street. The camera follows gently from behind. As she leaves the roof, raindrops visibly strike the canopy and the close umbrella patter returns. Hold her walking briefly through the end.

overall_soundscape: Distant city rain and soft traffic continue throughout. Nearby roof and umbrella rain remain thin at the beginning; as she steps into the rain, audible drops land on the canopy and the close umbrella patter returns. No dialogue or dramatic cue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 11 秒的雨夜公交站 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；公交候车棚、街道和雨夜灯光参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–2秒：从洛天依停住的握伞动作接起。她站在候车棚屋檐下，手持打开的透明伞，慢慢抬头望向街道；屋檐外的雨丝持续可见。
2. 镜头2 2–6.5秒：切到她望向的街道远景。暖色路灯亮在雨雾里，几辆车从湿润道路驶过，城市远处的山坡在雨雾中若隐若现。画面安静停留，街道上没有乐正绫身影或虚影。
3. 镜头3 6.5–11秒：切回洛天依的背影中景。她原本站在屋檐下，手持透明伞向前走出候车棚，镜头从后方缓缓跟随；走进雨里时，雨点重新落在伞面上。

【音频风格】
远处雨声与车流声始终持续，开头近处檐边和伞面雨声保持轻薄；她走出屋檐后，雨点重新敲在伞面，近处雨声逐渐回来。无对白，不另作配乐。

【运镜与核心约束】
先从握伞与抬头切至街道主观远景，再切回人物背影跟拍。洛天依自然撑伞，雨丝持续可见；地面湿润，只有局部小水洼。以切镜或后期雨伞遮挡衔接后续观景台，不要求本片段呈现完整路程。
```

## 剪辑与衔接

- 已检查 `output\shot19-20rear.mp4` 的尾帧：洛天依灰色袖口和握透明伞柄的手位于前景，雨夜道路与高架在背景。可以从这个手部近景切到她抬头；本提示词未将尾帧作为固定首帧，实际剪辑位置需以选用画面为准。
- 约第 2 秒切到街道主观远景，第 6.5 秒切回背影；最终对应剧本约 2:00 的切点和歌曲节奏。
- 前段近处滴水变稀疏、近处雨声变薄应继续保持；人物走出屋檐后，单独混入雨点落伞的近声。远处城市雨声跨切镜连续，不能用整体静音代替。
- 片尾走出站牌后，通过切镜或后期用行人雨伞遮挡，省略前往山坡观景台的路程，再接镜头 23；观景台与站牌不是同一地点，不能假定一镜走到。
- 如果一次生成中的主观远景和人物位置不稳定，可拆为抬头、街道远景、背影离开三个短镜，后期接合。下一组观景台尚需单独场景参考。
