from pipe_classes import PipeLine
import pytest
def test_convert_to_comercial():


    assert PipeLine.convertToComercial("",0.6) == "3/4"
    assert PipeLine.convertToComercial("",0.4) == "1/2"
    assert PipeLine.convertToComercial("",1) == "1 1/4"
    assert PipeLine.convertToComercial("",0.01) == "3/8"
    assert PipeLine.convertToComercial("",0.5) == "3/4"
    assert PipeLine.convertToComercial("",0) == "3/8"
    assert PipeLine.convertToComercial("",0.45) == "1/2"
    

    with pytest.raises(ValueError):
        PipeLine.convertToComercial("",4)

    with pytest.raises(ValueError):
        PipeLine.convertToComercial("",5)
    