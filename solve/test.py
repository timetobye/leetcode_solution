from os import listdir

"""
마크다운을 이용해 문제 풀이 결과를 적기 위한 코드입니다.
- 디렉토리 내 파일 리스트를 가져옵니다.
- 그리고 문항 번호를 슬라이싱 해서 웹에서 정보를 가져옵니다.
- 마크다운 양식에 맞게 프린트 한 후 정리합니다.

"""


def get_parsing_file_list():
    parsing_file_list = []

    current_folder_file_names = listdir('.')
    current_folder_file_names.remove('test.py')  # delete test.py file nmae in List

    for file_name in current_folder_file_names:
        if file_name[-2:] == 'py':
            file_name = file_name.replace(' ', '_')
            parsing_file_list.append(file_name)

    return parsing_file_list


def func(x):
    return int(x.split('_', 1)[0])


def sort_file_name_list(parsing_file_list):
    sorted_file_name_list = sorted(parsing_file_list, key=func)

    return sorted_file_name_list


def print_markdown_form(sorted_file_name_list):
    for i, file_name in enumerate(sorted_file_name_list):
        problem_number = file_name.split('_', 1)[0]  # str.split([sep[, maxsplit]])
        problem_title = file_name.split('_', 1)[1][:-3].replace(' ', '_')
        try:
            print(f'|{problem_number}|{problem_title}|'
                  f'[Link](https://github.com/timetobye/leetcode_solution/tree/master/solve/{file_name})'
                  f'|성공| |')

        except Exception as e:
            """숫자 문자열이 아니면"""
            pass


def main():
    parsing_file_list = get_parsing_file_list()
    sorted_file_list = sort_file_name_list(parsing_file_list)

    print_markdown_form(sorted_file_list)


if __name__ == "__main__":
    main()