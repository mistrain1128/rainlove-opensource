# 雨爱 · 日语填词翻唱 开源分享包

洛天依（ACE Studio）翻唱《雨爱》日语填词版的调教工程、MV 歌词字幕动画脚本、
剧本与分镜提示词的学习用分享包。**仅限非商业同人学习用途**，请先阅读
[NOTICE.md](NOTICE.md) 中的权利声明与署名要求。

## 目录结构

```
rainlove-opensource/
├── README.md                  本文件
├── LICENSE                    代码许可（MIT）
├── LICENSE-DOCS               文档/提示词/工程/截图许可（CC BY-NC-SA 4.0）
├── NOTICE.md                  权利声明、署名与授权清单（必读）
├── project/
│   ├── 雨爱.acep              ACE Studio 调教工程副本（7 条人声合成轨 + 3 条伴奏引用）
│   ├── README.md              工程素材清单与缺件说明
│   └── screenshots/           调教参数曲线截图（主歌 / 副歌）
├── lyrics/
│   └── rainlove_ja_zh.srt     日中双语字幕（46 条，字幕脚本的唯一歌词来源）
├── scripts/
│   ├── render_lyrics_v04.py   「雨滴凝字」双语歌词字幕渲染脚本（最终版）
│   ├── make_fonts.py          从 Noto Serif CJK 可变字体实例化静态字重的脚本
│   └── fonts/                 NotoSerifJP-Medium / NotoSerifSC-Regular + OFL 许可证
└── docs/
    ├── 01-短篇故事-雨还在下-Gemini4Hydrogen改写版.md
    ├── 02-完整时间轴剧本-雨还在下.md
    ├── scene_image_plan.md    场景图规划
    ├── scene_prompts_ordered.md / clean_scene_prompts_ordered.md
    └── video_prompts/         27 份分镜视频生成提示词（clip_01–clip_24 及补镜头）
```

分镜提示词中的 `MV/` 路径用于标识制作时使用的参考素材。参考图和视频未随包分发，复用提示词时请自行提供相应素材。

## 快速开始：渲染歌词字幕轨

依赖：Python ≥ 3.10、`pillow`、PATH 中有 `ffmpeg`（需支持 `qtrle` 编码）。

```bash
pip install pillow
cd scripts
python render_lyrics_v04.py RainLove_Lyric_Track.mov
```

- 输出 1920×1080、29.97fps、7873 帧（约 262.7s）的 **带 alpha 通道** QuickTime 动画字幕轨，
  可直接叠放在 MV 画面上层（DaVinci Resolve / Premiere / FFmpeg 均可）。
- 歌词与时间轴完全来自 `../lyrics/rainlove_ja_zh.srt`（脚本按相对路径读取，
  请保持 `scripts/` 与 `lyrics/` 的相对位置，或自行修改脚本中的 `ROOT` 指向）。
- 动画设计：逐字「凝入」（淡入 + 上浮 + 去焦）→ 停留 → 「沉出」（下沉 + 淡出 + 微 bloom）；
  日文行基线 y=930、中文行 y=984；`Rainie love` / `虹を信じてる` 两句带辉光强调。
- 全片渲染约需数十分钟（逐帧 PIL 合成 + 管道送 ffmpeg），属正常耗时。

## 打开调教工程

1. 安装 ACE Studio（本包工程保存于 CLI v0.18.7 对应版本）。
2. 打开 `project/雨爱.acep`。人声 7 轨为 ACE 合成轨（含 1 条备用空轨），**不依赖任何外部音频文件**，
   打开即可试听/编辑唱名、音高与参数曲线。
3. 3 轨伴奏（drums / bass / others）引用官方分轨音频，**因版权原因未随包分发**，
   打开时会显示缺件；不影响人声调教学习。详见 [project/README.md](project/README.md)。
4. 注意区分两个歌词层：唱名音符层为全假名（调教用）；编曲区第 3 行「歌词」栏为
   独立文本层（汉字假名混写，供阅读）。该栏文本已于 2026-11-19 按 SRT 校订完毕；
   如发现出入，以 `lyrics/rainlove_ja_zh.srt` 的日语为准。

## 许可

| 内容 | 许可 |
| --- | --- |
| `scripts/*.py` | MIT（[LICENSE](LICENSE)） |
| 剧本、提示词、SRT 编排、工程副本、截图 | CC BY-NC-SA 4.0（[LICENSE-DOCS](LICENSE-DOCS)） |
| `scripts/fonts/*.ttf` | SIL OFL 1.1（[fonts/LICENSE-OFL.txt](scripts/fonts/LICENSE-OFL.txt)） |
| 原曲词曲、官方伴奏、洛天依声库 | **不在授权范围内**，见 [NOTICE.md](NOTICE.md) |

CC BY-NC-SA 的「非商业」约束与原曲同人使用边界叠加生效：任何商业使用均需
另行取得原曲权利方与填词作者授权。

## 不包含的内容

- 官方伴奏分轨、原曲音频、参考视频（第三方版权）；
- 翻唱混音成品音频（含官方伴奏，不可再分发）；
- MV 片头标题与巴士车窗「雨愛」结尾签名的脚本及素材（作者保留，不开源）；
- DaVinci Resolve 工程与成片（含第三方素材与上述保留素材）。

## 署名示例

> 调教 / MV / 中文翻译：mist雾雨酱
>
> 原曲：《雨爱》（词 Wonderful ／ 曲 金大洲 ／ 编曲 黄宣铭 ／ 原唱 杨丞琳）
>
> 日语填词：[一灯大学士](https://www.bilibili.com/video/BV1sZZEBzE6E/) · 填词适配参考：[东洋雪莲的日语填词完整版](https://www.bilibili.com/video/BV1tpn96SEV5/)
>
> 演唱声库：洛天依（Vsinger，经 ACE Studio 合成）
>
> 本项目为非商业同人学习作品，与原作及 Vsinger 官方无关。
