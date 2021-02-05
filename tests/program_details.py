### 番組の詳細
data = {"programId":"239729","results":20,"areaId":"23","sort":"broadCastStartDate"}
url = "https://tv.yahoo.co.jp/api/adapter"
method = "POST"
headers = {
    "target-api": "mindsSiQuery",
    "target-path": "/TVWebService/V2/contents",
    "Origin": "https://tv.yahoo.co.jp",
    "Content-Type": "application/json;charset=utf-8"
}


######### START OF RESULT EXAMPLE
"""
{
    "ResultSet": {
        "attribute": {
            "totalResultsAvailable": 7,
            "totalResultsReturned": 7,
            "firstResultPosition": 0
        },
        "Result": [
            {
                "contentsId": "82068858",
                "programId": 239729,
                "eventDate": "20210130",
                "eventId": 29604,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1612562400,
                "broadCastEndDate": 1612564200,
                "duration": 1800,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x1"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "スポーツ"
                ],
                "minorGenreId": [
                    "0x0",
                    "0x2",
                    "0x0"
                ],
                "minorGenreName": [
                    "定時・総合",
                    "特集・ドキュメント",
                    "スポーツニュース"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本",
                "summary": "【７時台】届いたばかりのニュースを分かりやすくお届け。社会の深層に鋭く迫る特集。スポーツ、南さんの気象情報　など　【キャスター】新井秀和，石橋亜紗ほか",
                "descriptions": "[{\"note\":\"お出かけ前の今、知りたい！朝いちばんの最新情報が満載！けさの関心事やとれたてのニュースをわかりやすく生き生きとお伝えします！おでかけ＆お帰りの天気は？１日の天気を詳しく・きめ細かく！注目のスポーツを多角的にたっぷりとお見せします！特集では、政治、経済から社会問題、海外の話題、そしてくらしに役立つ情報など、幅広いジャンルにわたって、深く掘り下げてお伝えします。知りたい情報が一目でわかります！\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸，【スポーツキャスター】廣瀬智美\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-01-29T15:08:38Z",
                "updateTime": "2021-01-30T01:32:16Z",
                "_version_": 1690895466346053600
            },
            {
                "contentsId": "82068870",
                "programId": 239729,
                "eventDate": "20210130",
                "eventId": 29605,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1612564200,
                "broadCastEndDate": 1612566000,
                "duration": 1800,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x0"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "ニュース／報道"
                ],
                "minorGenreId": [
                    "0x9",
                    "0x1",
                    "0xA"
                ],
                "minorGenreName": [
                    "ローカル・地域",
                    "天気",
                    "交通"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本（関東甲信越）",
                "summary": "▽水戸藩の教えは今も　疫病退散だるまに願う　▽マスクの下で笑顔呼吸　【キャスター】新井秀和，石橋亜紗ほか",
                "descriptions": "[{\"note\":\"関東甲信越のニュースと気象情報▽週末行ってみたくなるあの場所から中継▽関東甲信越各地の魅力を発見する「すてき旅」▽目からうろこの生活情報「くらしり」▽特集も\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-01-29T15:08:38Z",
                "updateTime": "2021-02-05T02:55:31Z",
                "_version_": 1690895466349199400
            },
            {
                "contentsId": "82102404",
                "programId": 239729,
                "eventDate": "20210131",
                "eventId": 30737,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1612648800,
                "broadCastEndDate": 1612651200,
                "duration": 2400,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x1"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "スポーツ"
                ],
                "minorGenreId": [
                    "0x0",
                    "0x2",
                    "0x0"
                ],
                "minorGenreName": [
                    "定時・総合",
                    "特集・ドキュメント",
                    "スポーツニュース"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本",
                "summary": "【７時台】届いたばかりのニュースを分かりやすくお届け。社会の深層に鋭く迫る特集。スポーツ、南さんの気象情報　など　【キャスター】新井秀和，石橋亜紗ほか",
                "descriptions": "[{\"note\":\"お出かけ前の今、知りたい！朝いちばんの最新情報が満載！けさの関心事やとれたてのニュースをわかりやすく生き生きとお伝えします！１日の天気を３時間ごとにお見せするきめ細かい気象情報！注目のスポーツを多角的にたっぷりと！特集では、政治、経済から社会問題、海外の話題、くらしに役立つ情報、全国各地の旬の情報など、幅広いジャンルにわたって、深く掘り下げてお伝えします。知りたい情報が一目でわかります！\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸，【スポーツキャスター】廣瀬智美\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-01-30T15:09:40Z",
                "updateTime": "2021-01-31T01:22:18Z",
                "_version_": 1690895466529554400
            },
            {
                "contentsId": "82102410",
                "programId": 239729,
                "eventDate": "20210131",
                "eventId": 30738,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1612651200,
                "broadCastEndDate": 1612651500,
                "duration": 300,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0"
                ],
                "majorGenreName": [
                    "ニュース／報道"
                ],
                "minorGenreId": [
                    "0x0"
                ],
                "minorGenreName": [
                    "定時・総合"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本（関東甲信越）　ニュース・気象情報",
                "summary": "",
                "descriptions": "[]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-01-30T15:09:40Z",
                "updateTime": "2021-01-30T15:09:40Z",
                "_version_": 1690895466531651600
            },
            {
                "contentsId": "82308925",
                "programId": 239729,
                "eventDate": "20210206",
                "eventId": 34508,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1613163600,
                "broadCastEndDate": 1613167200,
                "duration": 3600,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x1"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "スポーツ"
                ],
                "minorGenreId": [
                    "0x0",
                    "0x2",
                    "0x0"
                ],
                "minorGenreName": [
                    "定時・総合",
                    "特集・ドキュメント",
                    "スポーツニュース"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "title": "ＮＨＫニュース　おはよう日本",
                "summary": "【６時台】土曜日も「おはよう日本」でアップデート！国内外で起きた最新のニュースをコンパクトにお届け！気象情報・スポーツもキュッとまとめてお伝えします。",
                "descriptions": "[{\"note\":\"お出かけ前の今、知りたい！朝いちばんの最新情報が満載！けさの関心事やとれたてのニュースをわかりやすく生き生きとお伝えします！おでかけ＆お帰りの天気は？１日の天気を詳しく・きめ細かく！注目のスポーツを多角的にたっぷりとお見せします！世界各地のニュースの現場を渾身のリポート。思わずほっこりするショートストーリー。おさえておきたいニュースをコンパクトに。知りたい情報が一目でわかります！\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸，【スポーツキャスター】廣瀬智美\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-02-05T15:09:54Z",
                "updateTime": "2021-02-05T15:24:13Z",
                "_version_": 1690895468025872400
            },
            {
                "contentsId": "82308935",
                "programId": 239729,
                "eventDate": "20210206",
                "eventId": 34513,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1613167200,
                "broadCastEndDate": 1613169000,
                "duration": 1800,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x1"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "スポーツ"
                ],
                "minorGenreId": [
                    "0x0",
                    "0x2",
                    "0x0"
                ],
                "minorGenreName": [
                    "定時・総合",
                    "特集・ドキュメント",
                    "スポーツニュース"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本",
                "summary": "【７時台】届いたばかりのニュースを分かりやすくお届け。社会の深層に鋭く迫る特集。スポーツ、南さんの気象情報　など　【キャスター】新井秀和，石橋亜紗ほか",
                "descriptions": "[{\"note\":\"お出かけ前の今、知りたい！朝いちばんの最新情報が満載！けさの関心事やとれたてのニュースをわかりやすく生き生きとお伝えします！おでかけ＆お帰りの天気は？１日の天気を詳しく・きめ細かく！注目のスポーツを多角的にたっぷりとお見せします！特集では、政治、経済から社会問題、海外の話題、そしてくらしに役立つ情報など、幅広いジャンルにわたって、深く掘り下げてお伝えします。知りたい情報が一目でわかります！\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸，【スポーツキャスター】廣瀬智美\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-02-05T15:09:54Z",
                "updateTime": "2021-02-05T15:24:13Z",
                "_version_": 1690895468029018000
            },
            {
                "contentsId": "82308945",
                "programId": 239729,
                "eventDate": "20210206",
                "eventId": 34514,
                "areaId": [
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29"
                ],
                "areaName": [
                    "東京",
                    "神奈川",
                    "群馬",
                    "茨城",
                    "千葉",
                    "栃木",
                    "埼玉"
                ],
                "siTypeId": 3,
                "siTypeName": "地上波",
                "networkId": "0x7FE0",
                "serviceId": "0x0400",
                "serviceName": "NHK総合1・東京",
                "channelNumber": 1,
                "channelSortOrder": 1,
                "broadCastStartDate": 1613169000,
                "broadCastEndDate": 1613170800,
                "duration": 1800,
                "broadCastStartTime": "07:00:03",
                "broadCastEndTime": "07:45:00",
                "week": [
                    "日"
                ],
                "majorGenreId": [
                    "0x0",
                    "0x0",
                    "0x0"
                ],
                "majorGenreName": [
                    "ニュース／報道",
                    "ニュース／報道",
                    "ニュース／報道"
                ],
                "minorGenreId": [
                    "0x9",
                    "0x1",
                    "0xA"
                ],
                "minorGenreName": [
                    "ローカル・地域",
                    "天気",
                    "交通"
                ],
                "programTitle": "NHKニュース おはよう日本",
                "element": [
                    "🈑"
                ],
                "title": "ＮＨＫニュース　おはよう日本（関東甲信越）",
                "summary": "関東甲信越のニュースと気象情報▽週末行ってみたくなるあの場所から中継▽関東甲信越各地の魅力を発見する「すてき旅」▽目からうろこの生活情報「くらしり」▽特集も",
                "descriptions": "[{\"note\":\"関東甲信越のニュースと気象情報▽週末行ってみたくなるあの場所から中継▽関東甲信越各地の魅力を発見する「すてき旅」▽目からうろこの生活情報「くらしり」▽特集も\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸\",\"title\":\"出演者\"}]",
                "broadCasterName": "NHK総合",
                "channelLogo": "https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                "mitaiCount": 2487,
                "reviewCount": 253,
                "ratingCount": 22,
                "ratingAverage": 1.82,
                "listingsFlg": true,
                "simpleListingsFlg": true,
                "dupListingsFlg": true,
                "eventGroup": false,
                "featureImage": "",
                "picturesContainer": "",
                "featureMovie": "",
                "movieUrlsContainer": "",
                "relationUrlsContainer": "[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                "createTime": "2021-02-05T15:09:54Z",
                "updateTime": "2021-02-05T15:24:13Z",
                "_version_": 1690895468031115300
            }
        ]
    }
}
"""


### OR PARSING THE WEBSITE

# --> https://tv.yahoo.co.jp/program/82068870 --> /program/<content_id>


######### START OF RESULT EXAMPLE

## location: <script id="__NEXT_DATA__" type="application/json">

"""
{
   "props":{
      "isServer":true,
      "initialState":{
         "authUser":{
            "cookie":{
               "guid":"",
               "isLogin":false
            },
            "loginUrl":"https://login.yahoo.co.jp/config/login?.src=tv\u0026.done=https%3A%2F%2Ftv.yahoo.co.jp%2Fprogram%2F82068870",
            "crumbToken":""
         },
         "searchOption":{
            "query":"",
            "areaId":"23",
            "siTypeIds":[
               "1",
               "3"
            ],
            "majorGenreId":"",
            "broadStartDate":"",
            "programElement":"",
            "duration":"",
            "broadCastHourMin":"",
            "broadCastHourMax":"",
            "hourChecked":0,
            "start":0,
            "sort":0
         },
         "mindsMaster":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":1,
                     "totalResultsReturned":1,
                     "firstResultPosition":0
                  },
                  "Result":[
                     {
                        "contentsId":"82068870",
                        "programId":239729,
                        "eventDate":"20210130",
                        "eventId":29605,
                        "areaId":[
                           "23",
                           "24",
                           "25",
                           "26",
                           "27",
                           "28",
                           "29"
                        ],
                        "areaName":[
                           "東京",
                           "神奈川",
                           "群馬",
                           "茨城",
                           "千葉",
                           "栃木",
                           "埼玉"
                        ],
                        "siTypeId":3,
                        "siTypeName":"地上波",
                        "networkId":"0x7FE0",
                        "serviceId":"0x0400",
                        "serviceName":"NHK総合1・東京",
                        "channelNumber":1,
                        "channelSortOrder":1,
                        "broadCastStartDate":1612564200,
                        "broadCastEndDate":1612566000,
                        "duration":1800,
                        "broadCastStartTime":"07:00:03",
                        "broadCastEndTime":"07:45:00",
                        "week":[
                           "日"
                        ],
                        "majorGenreId":[
                           "0x0",
                           "0x0",
                           "0x0"
                        ],
                        "majorGenreName":[
                           "ニュース／報道",
                           "ニュース／報道",
                           "ニュース／報道"
                        ],
                        "minorGenreId":[
                           "0x9",
                           "0x1",
                           "0xA"
                        ],
                        "minorGenreName":[
                           "ローカル・地域",
                           "天気",
                           "交通"
                        ],
                        "programTitle":"NHKニュース おはよう日本",
                        "element":[
                           "🈑"
                        ],
                        "title":"ＮＨＫニュース　おはよう日本（関東甲信越）",
                        "summary":"▽水戸藩の教えは今も　疫病退散だるまに願う　▽マスクの下で笑顔呼吸　【キャスター】新井秀和，石橋亜紗ほか",
                        "descriptions":"[{\"note\":\"関東甲信越のニュースと気象情報▽週末行ってみたくなるあの場所から中継▽関東甲信越各地の魅力を発見する「すてき旅」▽目からうろこの生活情報「くらしり」▽特集も\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸\",\"title\":\"出演者\"}]",
                        "broadCasterName":"NHK総合",
                        "channelLogo":"https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                        "mitaiCount":2487,
                        "reviewCount":253,
                        "ratingCount":22,
                        "ratingAverage":1.82,
                        "listingsFlg":true,
                        "simpleListingsFlg":true,
                        "dupListingsFlg":true,
                        "eventGroup":false,
                        "featureImage":"",
                        "picturesContainer":"",
                        "featureMovie":"",
                        "movieUrlsContainer":"",
                        "relationUrlsContainer":"[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                        "createTime":"2021-01-29T15:08:38Z",
                        "updateTime":"2021-02-05T02:55:31Z",
                        "_version_":1690895466349199400
                     }
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "mindsAll":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":1,
                     "totalResultsReturned":1,
                     "firstResultPosition":0
                  },
                  "Result":[
                     {
                        "contentsId":"82068870",
                        "programId":239729,
                        "eventDate":"20210130",
                        "eventId":29605,
                        "areaId":[
                           "23",
                           "24",
                           "25",
                           "26",
                           "27",
                           "28",
                           "29"
                        ],
                        "areaName":[
                           "東京",
                           "神奈川",
                           "群馬",
                           "茨城",
                           "千葉",
                           "栃木",
                           "埼玉"
                        ],
                        "siTypeId":3,
                        "siTypeName":"地上波",
                        "networkId":"0x7FE0",
                        "serviceId":"0x0400",
                        "serviceName":"NHK総合1・東京",
                        "channelNumber":1,
                        "channelSortOrder":1,
                        "broadCastStartDate":1612564200,
                        "broadCastEndDate":1612566000,
                        "duration":1800,
                        "broadCastStartTime":"07:00:03",
                        "broadCastEndTime":"07:45:00",
                        "week":[
                           "日"
                        ],
                        "majorGenreId":[
                           "0x0",
                           "0x0",
                           "0x0"
                        ],
                        "majorGenreName":[
                           "ニュース／報道",
                           "ニュース／報道",
                           "ニュース／報道"
                        ],
                        "minorGenreId":[
                           "0x9",
                           "0x1",
                           "0xA"
                        ],
                        "minorGenreName":[
                           "ローカル・地域",
                           "天気",
                           "交通"
                        ],
                        "programTitle":"NHKニュース おはよう日本",
                        "element":[
                           "🈑"
                        ],
                        "title":"ＮＨＫニュース　おはよう日本（関東甲信越）",
                        "summary":"▽水戸藩の教えは今も　疫病退散だるまに願う　▽マスクの下で笑顔呼吸　【キャスター】新井秀和，石橋亜紗ほか",
                        "descriptions":"[{\"note\":\"関東甲信越のニュースと気象情報▽週末行ってみたくなるあの場所から中継▽関東甲信越各地の魅力を発見する「すてき旅」▽目からうろこの生活情報「くらしり」▽特集も\",\"title\":\"番組内容\"},{\"note\":\"【キャスター】新井秀和，石橋亜紗，【気象キャスター】南利幸\",\"title\":\"出演者\"}]",
                        "broadCasterName":"NHK総合",
                        "channelLogo":"https://tv-pctr.c.yimg.jp/d/tv-image/logo/7FE0-0400/46x46/logo-7FE0-011-46x46.png",
                        "mitaiCount":2487,
                        "reviewCount":253,
                        "ratingCount":22,
                        "ratingAverage":1.82,
                        "listingsFlg":true,
                        "simpleListingsFlg":true,
                        "dupListingsFlg":true,
                        "eventGroup":false,
                        "featureImage":"",
                        "picturesContainer":"",
                        "featureMovie":"",
                        "movieUrlsContainer":"",
                        "relationUrlsContainer":"[{\"type\":\"ALL\",\"categoryId\":\"PUBLIC\",\"title\":\"番組公式サイト\",\"url\":\"https://www.nhk.jp/p/ohayou/ts/QLP4RZ8ZY3/\",\"publishStartDate\":1427382000,\"publishEndDate\":1924959599}]",
                        "createTime":"2021-01-29T15:08:38Z",
                        "updateTime":"2021-02-05T02:55:31Z",
                        "_version_":1690895466349199400
                     }
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "mindsTalent":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "talent":{
            "data":{
               "ResultSet":{
                  "Results":{
                     "Person":[
                        
                     ]
                  }
               }
            },
            "error":"",
            "loading":false
         },
         "gyaoWeb2App":{
            "data":{
               "result":{
                  "result_id":239729,
                  "result_id_type":"tv",
                  "return_count":0,
                  "total_count":0
               },
               "items":[
                  
               ]
            },
            "error":"",
            "loading":false
         },
         "gyaoWeb2AppList":{
            "data":{
               
            },
            "gyaoList":[
               
            ],
            "error":{
               
            },
            "loading":false
         },
         "commentHistory":{
            "data":{
               "message":""
            },
            "error":"",
            "loading":false
         },
         "comments":{
            "data":{
               "ResultSet":{
                  "attributes":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "topics":{
            "data":{
               "ResultSet":{
                  "attributes":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "myTotalVotes":{
            "total":0,
            "error":"",
            "loading":false,
            "loaded":false
         },
         "myMitai":{
            "loading":false,
            "reload":false,
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":""
         },
         "myReview":{
            "loaded":false,
            "loading":false,
            "reload":false
         },
         "commentPost":{
            "data":{
               "result":{
                  "comment_id":"",
                  "status":""
               }
            },
            "request":{
               "title":"",
               "text":""
            },
            "errorMessage":{
               "title":"",
               "text":"",
               "response":""
            },
            "error":"",
            "loading":false
         },
         "commentRanking":{
            "data":{
               "Result":[
                  
               ]
            },
            "error":"",
            "loading":false
         },
         "commentVotes":{
            "data":{
               "result":{
                  "comment_id":"",
                  "status":""
               }
            },
            "error":"",
            "loading":false
         },
         "commentDelete":{
            "data":{
               "result":{
                  "comment_id":"",
                  "status":""
               }
            },
            "request":{
               "topicId":"",
               "commentId":""
            },
            "error":"",
            "loading":false
         },
         "commentReports":{
            "data":{
               "result":{
                  "comment_id":"",
                  "status":""
               }
            },
            "request":{
               "topicId":"",
               "commentId":"",
               "title":"",
               "item":"",
               "text":""
            },
            "errorMessage":{
               "item":"",
               "text":""
            },
            "error":"",
            "loading":false
         },
         "postWish":{
            "data":{
               "ResultSet":{
                  "Result":{
                     "Message":""
                  }
               }
            },
            "request":{
               
            },
            "error":"",
            "loading":false
         },
         "getWish":{
            "data":{
               "value":[
                  
               ]
            },
            "allWishData":{
               "value":[
                  
               ]
            },
            "error":"",
            "allWishError":"",
            "loading":false,
            "allWishLoading":false,
            "allWishLoaded":false
         },
         "getReview":{
            "data":{
               "value":{
                  
               }
            },
            "error":"",
            "loading":false
         },
         "postReview":{
            "data":{
               "ResultSet":{
                  "attributes":{
                     "status":""
                  }
               }
            },
            "error":"",
            "loading":false
         },
         "programUgc":{
            "data":{
               "reviewCount":0,
               "wishCount":0,
               "ratingAverage":0,
               "ratingCount":0
            },
            "error":"",
            "loading":false
         },
         "programListing":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "programListingSearchOption":{
            "siTypeId":"tv",
            "broadCastStartDate":"",
            "areaId":"23"
         },
         "withDetail":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "yvpListing":{
            "data":{
               "ResultSet":{
                  "totalResultsAvailable":0,
                  "totalResultsReturned":0,
                  "firstResultPosition":0,
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false
         },
         "shannonNews":{
            "data":{
               "responseHeader":{
                  "params":{
                     
                  }
               },
               "response":{
                  "numFound":0,
                  "docs":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false,
            "detailData":{
               "responseHeader":{
                  "params":{
                     
                  }
               },
               "response":{
                  "numFound":0,
                  "docs":[
                     
                  ]
               }
            },
            "detailError":"",
            "detailLoading":false
         },
         "mindsSiTop":{
            "data":{
               "ResultSet":{
                  "attribute":{
                     "totalResultsAvailable":0,
                     "totalResultsReturned":0,
                     "firstResultPosition":0
                  },
                  "Result":[
                     
                  ]
               }
            },
            "error":"",
            "loading":false,
            "loaded":false
         },
         "incaTool":{
            
         },
         "newsArchive":{
            "newsData":[
               
            ],
            "newsError":"",
            "loadedId":[
               
            ],
            "newsLoading":false,
            "nextStart":0,
            "hasMore":true
         },
         "udb":{
            "yid":"",
            "displayName":"",
            "displayIcon":"https://s.yimg.jp/images/gyao/v1/images/icon/user-gray.svg",
            "currentUrl":"https://tv.yahoo.co.jp/program/82068870",
            "regional":"",
            "now":1612564027858,
            "page":"detail",
            "device":"pc"
         },
         "menu":{
            "isOpen":false
         },
         "setRegional":{
            "data":false,
            "error":"",
            "loading":false
         },
         "emg":{
            "data":{
               "results":[
                  
               ]
            },
            "error":"",
            "loading":false
         },
         "cache":{
            
         }
      },
      "initialProps":{
         "pageProps":{
            "contentsId":"82068870"
         }
      }
   },
   "page":"/program",
   "query":{
      "contentsId":"82068870"
   },
   "buildId":"VBusPbzpQ0KTwqAgNa3T7",
   "isFallback":false,
   "customServer":true,
   "gip":true,
   "appGip":true
}
"""