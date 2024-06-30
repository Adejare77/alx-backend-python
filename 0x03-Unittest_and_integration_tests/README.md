# Unittests and Integeration Tests

`unittests.mock()` allows you to replace parts of your system under test with mock objects and make assertions about hwo they have been used.
I provides a core `Mock` class removing the need to create a host of stubs through your test suite. After performing an action, you can mkae assertions about which methods/attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.
Additionally, `mock` provides a `patch()` decorator that handles patching module and class level attributes within the scope of a test, along with sentinel for creating unique objects.
Mock is designed for use with `unittest` and is based on the "action -> assertion" pattern instead of "record -> replay" used by many mocking frameworks

## Mock and MagicMock

Both `Mock` and `MagicMock` objects create all attributes and methods as you access them and store details fo how they have been used. You can configure them to specify return values or limit what attributes are available, and then make assertions about hwo they have been used.

`Mock`: is a general purpose mock object that can be used to replace real objects in your tests. It can be configured to return specific values, raise exceptions, call functions or check how it was called. We use `Mock` when you want a simple object to simulate a real one. You can set the `return_value`, `side_effects`, `specs` etc and tracked how the mock is used.

`MagicMock`: is a subclass of `Mock()` with additional 'Magic methods'. The Magic methods include: __len__, __getitem__, __setitem__, __iter__, etc. Basically, defaults dunder attributes are created. Use `MagicMock` when you need to mock an object that reuqires 'Magic methods'. For instance, if you need to mock an object that behaves like a container or has special dunder behaviour.

### Spec, Patch
