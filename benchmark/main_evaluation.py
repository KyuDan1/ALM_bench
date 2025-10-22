## TO DO
## dataset download


## TODO
## model download or api load


## TODO
## form input


## TODO
## input model and get output


## TODO
## benchmark evaluation

## TODO
## print..
import argparse


def main():
    # 인자값을 받을 수 있는 인스턴스 생성
    parser = argparse.ArgumentParser(description='Benchmark Evaluation')

    # 입력받을 인자값 설정 (default 값 설정가능)
    parser.add_argument('--model', type=str, default='gemini-2.5-flash')
    parser.add_argument('--benchmark', type=str, default='mmau-test-mini')
    parser.add_argument('--device', type=str, default='cuda:0')
    parser.add_argument('--batch_size', type=int, default=8)

    # args 에 위의 내용 저장
    args    = parser.parse_args()

    # 입력받은 인자값 출력
    print(args.model)
    print(args.benchmark)
    print(args.device)
    print(args.batch_size)


main()
