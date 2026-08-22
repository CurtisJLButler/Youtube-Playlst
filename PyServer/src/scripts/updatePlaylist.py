from typing import List

video = {
    "_id": 0,
    "thumbnail": "https://i.ytimg.com/vi/7h7bnYA1LXE/default.jpg",
    "title": "【東方MV】スカーレット警察のゲットーパトロール24時【IOSYS】",
    "description": "#あたいの足技みさらせやー\n\nフル尺音源\nhttps://www.youtube.com/watch?v=l8_DCg0363U\nMV Editインスト音源\nhttps://www.iosysos.com/data/IO-0285_07_mv_inst.wav\n歌詞テキスト\nhttps://www.iosysos.com/data/IO-0285_07_mv_lyric.txt\n字幕ファイル\nhttps://www.iosysos.com/data/IO-0285_07_mv.sbv\nMMD用のモーションデータ\nhttps://www.iosysos.com/data/sgp24_MMD.zip\n\n＜スカーレット警察シリーズMVリンク＞\nイタ電はやめて！ ぼくらのスカーレット・コール\nhttps://www.youtube.com/watch?v=xcGd_NZaZKw\n\n07．スカーレット警察のゲットーパトロール24時 / 七条レタスグループ\n原曲：おてんば恋娘, 亡き王女の為のセプテット\n作詞：七条レタス (IOSYS)\n編曲：D.watt (IOSYS)\n\n声の出演\nチルノ: miko (Alternative Ending)\nレミリア(署長): ココ (Innocent Key)\n咲夜(ナイフ): 96 (IOSYS)\nパチュリー(もやし): 岩杉夏\n\nPV製作: 216 as VJ_frmk (Office-φ)\n\n収録アルバム：IO-0285 GENSOKYO DEMPA EXPO　─イオシス東方コンピレーション vol.23─\n\n「幻想郷のポップカルチャーは、世界に通用する文化である」\n誰が言ったか知らないが、人はこう呼ぶ\n～COOL GENSOKYO～\n2年ぶりに登場、イオシススタッフ結集による東方アレンジアルバム第23弾！\n「世界に届けたい2015年の電波ソング」をテーマに、\n最新のサウンドを集めた“プログレッシブな”電波ソング中心のコンピレーションです。\nトラックリスト\n01. 万博宣言\n02. 幻想郷DEMPASTICグリーティング\n03. プレイヤーがじゃぶじゃぶ信仰したくなるような射幸心を煽りまくるタイトル\n04. デュラハンナイト ～ 君の首、飛んで花火\n05. 紫雨UNITED まりさvsニセまりさ編\n06. 恋の氷結おてんば湯けむりチルノ温泉 (DJ Laugh Remix)\n07. スカーレット警察のゲットーパトロール24時\n08. Zombie Dance\n09. バブミーベイベー\n10. COOL GENSOKYO\n\nProducer　D.watt (IOSYS)\nDirector　七条レタス (IOSYS)\nDesk　96 (IOSYS), 夕野ヨシミ (IOSYS)\nMastering　uno (IOSYS)\nIllustration　モタ (motor home)\nPackage Design　オタクブックス\n\n2015.5.10 Release\nhttps://www.iosysos.com/discographyportal.php?cdno=IO-0285\n\n全ての原曲は「上海アリス幻樂団」のZUN氏によって作曲されたものです。",
    "video_id": "7h7bnYA1LXE"
}



def update(playlist, request):
    print(playlist)
    id = 0
    collection = request.app.database["videos"]
    # if collection.count() == 0:
    request.app.database["videos"].drop()

    for video in playlist:
        new_video = {
            "_id" : id,
            "thumbnail" : video["thumbnail"],
            "title" : video["title"],
            "description" : video["description"],
            "video_id" : video["video_id"]

        }
        new_video = request.app.database["videos"].insert_one(new_video)
        created_video = request.app.database["videos"].find_one()
        print(created_video)
        id += 1
    return created_video