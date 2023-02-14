from mypackage import myModule

def test_top_n():
    """
    make sures top_n works correctly
    """
    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], "incorrect"
    assert myModule.top_n([34,3,2,7,4], 3) == [34,7,4], "incorrect"
    assert myModule.top_n([12,3,2,10,4], 3) == [12,10,4], "incorrect"