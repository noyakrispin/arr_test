def test(temp_input):
    set_endpoints = temp_input[2].strip('()').split(',')
    set_endpoints_dict = {key: True for key in set_endpoints}
    connections = temp_input[1].strip('()').split(',')
    result = []
    for connection in connections:
        first_endpoint = connection[0]
        second_endpoint = connection[2]
        if not set_endpoints_dict.get(first_endpoint) and not set_endpoints_dict.get(second_endpoint):
            result.append(connection)

    print(result if len(result) else 'yes')


if __name__ == '__main__':
    temp_input = ['(A,B,C,D)', '(A-B,B-C,C-D)', '(A,C)']
    test(temp_input)

