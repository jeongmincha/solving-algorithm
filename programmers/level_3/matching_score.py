def solution(word, pages):
    import re

    meta_parser = re.compile('<meta(.+?)/>')
    a_parser = re.compile('<a(.+?)>')

    info = {}
    pages = [page.lower() for page in pages]

    for idx, page in enumerate(pages):
        url = meta_parser.findall(page)[0].split("content=")[-1]
        a = a_parser.findall(page)
        a = [e.split("href=")[-1] for e in a]
        
        default_score = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
        info[url] = {
            'index': idx,
            'score': {
                'link': 0,
                'total': default_score,
                'default': default_score
            },
            'content': page,
            'outlinks': a
        }
        if len(a) > 0:
            info[url]['score']['link'] = info[url]['score']['default'] / len(a)

    scores = [0] * len(pages)   
    for url in info.keys():
        for outlink in info[url]['outlinks']:
            if outlink in info:
                info[outlink]['score']['total'] += info[url]['score']['link']
    
    for url in info.keys():
        scores[info[url]['index']] = info[url]['score']['total']

    return scores.index(max(scores))


if __name__ == '__main__':
    test_cases = [
        (('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]), 0),
        (('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]), 1)

    ]
    for test_case in test_cases:
        word, pages = test_case[0]
        expected = test_case[1]
        answer = solution(word, pages)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
