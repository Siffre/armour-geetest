# ArmourGeeTest

>[TOS]
>- 本项仅供交流学习，有疑问请在[issue](https://github.com/QIN2DIM/armour-geetest/issues)中提出；
>- 本项目不提供面向任何商业需求的版本迭代；
>- 关于本项目的分享请遵循Apache-2.0 License；
>- 禁止任何人使用本项目及其分支提供任何形式的收费代理服务。

## :carousel_horse: 项目简介

1. [ArmourGeeTest](https://github.com/QIN2DIM/armour-geetest)是一种针对[GeeTest](https://www.geetest.com/)滑动验证的高通过率解决方案。

2. 引入`姿态收敛`以及`惯性牵引`等初中物理概念解决二维空间中的像素对齐问题。

3. 当这个难倒了大批爬虫玩家的问题被抽象成`缺口识别`以及`像素对齐`两个指标时使用本方案进行百次实验：

    - 当`缺口识别率`为100%时，`gt3`通过率为92%。失败案例中超半数由收敛超时引发，剩下的被怪兽吃掉了；
    
    - 当`缺口识别率`为100%时，`gt2`通过率100%。仅在缺口被遮挡时失败，但此时倾向认为`缺口识别率`<100%；
    
4. `gt3` 算子收敛过程小概率出现“震荡”现象，此时（为保证通过率）任务耗时将大幅增长，开发者可通过优（手）化（调）本项目的模型超参数，达成`低耗时`+`高通过率`的性能指标。

## :airplane:快速上手

- **【方案一】用户**

  通过观看[ArmourGeeTest滑动验证](https://www.yuque.com/docs/share/70b51b3c-b434-4e7f-b18a-62c806108488?#)demo了解本项目的工作范围。

- **【方案二】开发者**

  Clone项目，根据[技术文档](https://github.com/QIN2DIM/sspanel-geetest/blob/main/docs/subs/技术文档.md)合理配置`config.py`后编译项目。

## :ocean: 网上冲浪

- :gear: [技术文档](https://github.com/QIN2DIM/sspanel-geetest/blob/main/docs/subs/技术文档.md)

- :small_red_triangle: [注意事项](https://github.com/QIN2DIM/sspanel-geetest/blob/main/docs/subs/注意事项.md)

- :loudspeaker: [更新日志](https://github.com/QIN2DIM/sspanel-geetest/blob/main/docs/subs/更新日志.md)
- :world_map: [开源计划](https://github.com/QIN2DIM/sspanel-geetest/blob/main/docs/subs/开源计划.md)
