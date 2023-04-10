import csv

with open("CSV/singerA.csv", "r",encoding= 'utf-8') as inFpA :
    with open("CSV/singerB.csv", "r",encoding= 'utf-8') as inFpB:
        with open("CSV/singer165.csv", "w",encoding= 'utf-8' ,newline='') as outFp:
            # csvReaderA = csv.reader(inFpA)
            # csvReaderB = csv.reader(inFpB)
            # csvWriter = csv.writer(outFp)
            # header_list = next(csvReaderA)
            # header_list = next(csvReaderB)
            # csvWriter.writerow(header_list)

            # for row_list in csvReaderA:
            #     csvWriter.writerow(row_list)
            # for row_list in csvReaderB:
            #     csvWriter.writerow(row_list)

            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)

            # 헤더를 쓰기
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            # 평균키가 165 이상인 그룹의 데이터만 선택해서 쓰기
            for csvReader in [csvReaderA, csvReaderB]:
                rows = []
                for row in csvReader:
                    try:
                        height = float(row[2])
                        if height >= 165:
                            rows.append(row)
                    except ValueError:
                        pass
                for row in rows:
                    csvWriter.writerow(row)

print('Save. OK~')