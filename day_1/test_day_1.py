from day_1 import getListDistances_part_1

def test_getListDistances_part_1(monkeypatch):
    def mock_parse_lists(fileName):
        return ([1, 2, 3], [4, 5, 6])
    
    monkeypatch.setattr('day_1.parse_lists', mock_parse_lists)
    
    response = getListDistances_part_1()
    
    assert response == 9  # Expected output sum of distances