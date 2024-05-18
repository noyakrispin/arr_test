def test(temp_input):
    set_endpoints = extract_data(temp_input[2])
    set_endpoints_dict = {key: True for key in set_endpoints}
    connections = extract_data(temp_input[1])
    result = []
    for connection in connections:
        first_endpoint, second_endpoint = extract_endpoints(connection)
        if not set_endpoints_dict.get(first_endpoint) and not set_endpoints_dict.get(second_endpoint):
            result.append(connection)

    print(result if len(result) else 'yes')


def extract_data(data):
    return data.strip('()').split(',')


def extract_endpoints(connection):
    return connection[0], connection[2]


if __name__ == '__main__':
    temp_input = ['(A,B,C,D)', '(A-B,B-C,C-D)', '(A,C)']
    test(temp_input)
