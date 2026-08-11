import pytest
from app.operations import (
    OperationFactory, Addition, Subtraction, Multiplication, Division,
    Power, Root, Modulus, IntegerDivision, Percentage, AbsoluteDifference
)
from app.exceptions import OperationError, ValidationError

def test_concrete_operations_directly():
    assert Addition().execute(10, 5) == 15
    assert Subtraction().execute(10, 5) == 5
    assert Multiplication().execute(10, 5) == 50
    assert Division().execute(10, 5) == 2.0
    assert Power().execute(2, 3) == 8
    assert Root().execute(16, 2) == 4.0
    assert Modulus().execute(10, 3) == 1
    assert IntegerDivision().execute(10, 3) == 3
    assert Percentage().execute(20, 100) == 20.0
    assert AbsoluteDifference().execute(5, 10) == 5

def test_operation_errors():
    with pytest.raises(OperationError):
        Division().execute(5, 0)
    with pytest.raises(OperationError):
        Root().execute(16, 0)
    with pytest.raises(OperationError):
        Root().execute(-16, 2)
    with pytest.raises(OperationError):
        Modulus().execute(10, 0)
    with pytest.raises(OperationError):
        IntegerDivision().execute(10, 0)
    with pytest.raises(OperationError):
        Percentage().execute(10, 0)

def test_operation_factory():
    assert isinstance(OperationFactory.create('add'), Addition)
    assert isinstance(OperationFactory.create('subtract'), Subtraction)
    assert isinstance(OperationFactory.create('multiply'), Multiplication)
    assert isinstance(OperationFactory.create('divide'), Division)
    assert isinstance(OperationFactory.create('power'), Power)
    assert isinstance(OperationFactory.create('root'), Root)
    assert isinstance(OperationFactory.create('modulus'), Modulus)
    assert isinstance(OperationFactory.create('int_divide'), IntegerDivision)
    assert isinstance(OperationFactory.create('percent'), Percentage)
    assert isinstance(OperationFactory.create('abs_diff'), AbsoluteDifference)

def test_invalid_factory_key():
    with pytest.raises(ValidationError):
        OperationFactory.create('invalid_op')
