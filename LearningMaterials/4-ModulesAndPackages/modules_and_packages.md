# Modules and Packages

Modules and packages are two essential components that facilitate modularity, one of the foundational principles of clean code. Modularity involves breaking down code into smaller, self-contained units of functionality, each responsible for performing a specific task. This has several benefits:

- Logic in modules and packages can be reused elsewhere.
- Modules and packages allow for better code design and separation of responsibilities.

Simply put, **modules** are Python files, containing code, such as functions and variables, encapsulating specific functionalities or data. On the other hand, **packages** are collections of related modules (and sub-packages) organised hierarchically within directories.

## Modules

Modules are primarily made to be used in other modules or other parts of a Python program. To "use" a module means to access and utilise the objects defined within that module in your Python code.

To do this, we have to import the module into our code.

### Importing Modules

Suppose we have a module `example_module` which has the following contents:

```Python
# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


print("Hello world!")

```

There are a few different ways of importing this module into into our program:

1. **Using `import`**  

    Importing a module using the `import <module_name>` syntax means that any functions, classes, variables, or other objects defined within that module become available for use in your code. To access these objects, you use the dot notation, combining the module name with the specific object name you want to use.  

    **Note**: The name of a module is derived from the file name without the `.py` extension.

    In the above case, after importing `example_module`, we can access the functions `add` and `subtract` as follows:

    ```Python
    # my_script.py
    import example_module

    add_result = example_module.add(1, 2)
    subtract_result = example_module.subtract(1, 2)

    ```

    It's important to note that after executing `my_script.py`, you will see `'Hello world!'` printed out, despite no explicit `print('Hello world')` in this file. This is because when a module is imported, Python runs all the code in that module, before loading all objects defined in that module into the namespace of our code (through the name of the imported module). So in the line `import example_module`, the entirity of the code in `example_module` is executed, including the `print('Hello world!')`. Only after that are `add` and `subtract` then made accessible within `my_script.py` using the dot notation.

2. **Using `from` and `import`**

    Alternatively, you can import specific objects from a module directly into the current namespace using the `from <module_name> import <symbol>` syntax. This approach allows you to access the imported objects without needing to prefix them with the module name. It does mean that only the object specified from the module is made accessible.

    For example, we can import the `add` function directly from the `example_module` module. What this means is we can now access the `add` function as follows:

    ```Python
    # my_script.py
    from example_module import add

    add_result = add(1, 2)

    ```

    Since we only have imported the `add` function, we do not have access to the `subtract` function.

    After executing `my_script.py`, you will see `'Hello world!'` printed out. Whilst only one object from the module has been imported, Python still has to execute the whole module before loading that object directly into the namespace of our code.

3. **Using `as`**

    The `as` keyword in Python allows you to alias imported modules or objects with a different name.

    For example, we can import `example_module` but alias it as `ex_m`. What this then means is we can use the alias `ex_m` to access objects from `example_module`:

    ```Python
    # my_script.py
    import example_module as ex_m

    add_result = ex_m.add(1, 2)

    ```

    Similarly, you can use `as` with the `from ... import ...` syntax to alias imported objects:

    ```Python
    # my_script.py
    from example_module import add as ex_m_add

    add_result = ex_m_add(1, 2)

    ```

### Executing Modules as the Main Program

Since modules are Python files, they can be executed directly as shown in `1-PythonFile` as well as being imported elsewhere.

Because of the versatility, a very common construct used in Python files is the conditional expression `if __name__ == '__main__'`.
In short, this construct allows you to execute code when the module is run directly, but not when it is imported as a module elsewhere.

#### How `if __name__ == '__main__'` works

- When you run a Python file directly (e.g., `python example_module.py` or `python -m example_module`), Python assigns the special variable `__name__` to `'__main__'`, indicating that this script is the main program being executed.
- When you import a Python file as a module into another script (e.g., `import example_module`), Python assigns `__name__` to the name of the module (`'example_module'` in this case), indicating that it is being imported.
- Therefore, by using this construct, you can include code that should only be executed when the file is run directly, and not when it's imported as a module.  This avoids unintended behavior when importing modules.

For instance, suppose the code in `example_module` was updated with the following content:

```Python
# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return f"num_1 - num_2 is: {num_1 - num_2}"


print(f"__name__ is currently: {__name__}")

if __name__ == "__main__":
    print("This code is only executed when the module is run as a script.")

```

In this example, the `print(f"__name__ is currently: {__name__}")` statement will always execute regardless of how the module is used. However, the code block under `if __name__ == '__main__':` will only execute if the module is run directly, since this is the scenario when `__name__` is set to `"__main__"`. When the module is imported, `__name__` will be set to `'example_module'`, meaning the code block will not execute.

#### Adding a `main()` function

In Python, it's a common practice to define a `main()` function to encapsulate the main logic of the script. This improves readability, allows for better organisation, and makes the script easier to test. The `main()` function can be called within the `if __name__ == '__main__'` block to ensure that it only runs when the script is executed directly, not when it is imported as a module.

Here's how you can incorporate a `main()` function into the code:

```Python
# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return f"num_1 - num_2 is: {num_1 - num_2}"


def main():
    print("This is the main function executing.")
    result_add = add(5, 3)
    result_subtract = subtract(5, 3)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")


print(f"__name__ is currently: {__name__}")

if __name__ == "__main__":
    main()  
```

**Note**: Whilst it is common for this function to be called `main()`, it can have any name.

## Packages

Packages allow a collection of modules and subpackages (packages within a package) to be grouped together under a common package name.

Essentially a package is a directory containing Python modules and subpackages. These directories contain a special file named `__init__.py`, (unless using a [namespace package](https://docs.python.org/3/glossary.html#term-namespace-package), which is beyond the scope of this course), which will be executed upon importing the package or any of its modules / subpackages. While the `__init__.py` file is often left empty, since it is executed on importation, it can contain initialisation code such as importing modules or subpackages within the package, defining package-level objects or setting up configurations.

### Importing with Packages

#### **Importing a Module within a Package**

The syntax for importing modules from a package closely resembles that of importing a standalone module. The key distinction lies in specifying the module's path, which utilises dot notation. This notation combines the package name, any subpackages, if applicable, and finally the module name itself, all separated by dots.

In this directory there is a package provided with the following structure:

``` text
package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

1. **Using `import`**

    This imports an entire module into our script.

    ```Python
    # my_script.py
    import package.module1
    package.module1.mod1_function()
    ```

    In this case, we import the entire `mymodule1` into our script, and then we can access its functions using dot notation.

2. **Using `from` and `import`**

    Depending on its useage, this will either import an entire module into our code or a specific object defined within a module.

    ```Python
    # my_script.py
    from package import module2
    module2.mod2_function()
    ```

    Here, we are importing the entire `mymodule2` into our script, so we have access to all objects defined within through the dot notation.

    ```Python
    # my_script.py
    from package.module2 import mod2_function
    mod2_function()
    ```

    Here, we import only the function `mod2_function` into our script.

3. **Using `as`**

    ```Python
    # my_script.py
    from package.subpackage import module3 as m3
    m3.mod3_function()
    ```

    In all of these cases, the `__init__.py` file of `mypackage` is executed upon importation. Similarly, when importing from within subpackage, the `__init__.py` file of subpackage is also executed.

#### **Importing a Package / Subpackage**

Above we have imported a modules and objects from within a package. It is possible to import a package into your code as well.

For example, you can do the following:

```Python
# my_script.py
import package
```

What's important to note is that this action does not inherently grant access to the package's modules, subpackages, or submodules. What it does is create an empty namespace `packackage` as well as execute the package's `__init__.py` file. Therefore, if you want to ensure that some of the contents of the package are accessible upon import, it is essential to define what gets imported in the `__init__.py` file of the package.

For example, to ensure that `module1` is always accessible when `package` is imported you can include this in the `__init__.py` file of `package`:

```Python
# package/__init__.py
from package import module1
```

This is known as making `module1` a package-level module. Anything you import or define in this `__init__.py` would have the package-level title, since it will be accessible directly from the package namespace.

An example of importing in the `__init__.py` file can be found in the `requests` package. The typical use case of importing this package is to do as follows:

```Python
import request
```

What this does is import the requests package into our code, which will execute the `__init__.py`. This file in turn imports further modules and subpackages from within the `requests` package. This allows us to use the `get` function defined within that package.

## How to Split Up Code into Modules and Subpackages

### 1. Identify Logical Units in Your Code

Start by identifying logical components of your application or script that can be grouped into separate modules. Each module should have a clear, distinct responsibility.

For example, if you're building an e-commerce application, you might have modules for user authentication, product management, order processing, etc.

### 2. Create Modules for Each Logical Unit

Once you've identified the logical components, create a separate module for each unit. Each module should be focused on one task or related set of tasks.

For instance:

``` text
ecommerce/
├── __init__.py
├── user_auth.py
├── product_management.py
├── order_processing.py
└── payment_gateway.py
```

Each file represents a module that handles a specific responsibility.

### 3. Create Subpackages to Further Organise Code

As your project grows, you might need to organize certain modules into even smaller subgroups. This is where subpackages come in. A subpackage is simply a package within a package, which can further help in structuring large projects.

For example, you can create a payments subpackage to handle everything related to payment processing:

``` text
ecommerce/
├── __init__.py
├── user_auth.py         # User authentication module
├── product_management.py # Product management module
└── payments/
    ├── __init__.py
    ├── payment_gateway.py  # Payment gateway integration
    └── invoice.py           # Invoice generation
```

The payments/ directory is a subpackage that groups related modules, like `payment_gateway.py` and `invoice.py`.

What is important to note is that there is not only **one** right way to split up your code - it is a judgement call. The best practices to keep in mind during the modularisation process are:

- **Keep modules small and focused**: Each module should have a single responsibility. Avoid having large files with unrelated code.
- **Use meaningful names**: Name your modules and packages after the functionality they provide. For instance, `user_auth.py` should handle user authentication, and `product_management.py` should handle product-related operations.
- **Avoid circular imports**: Circular imports occur when two or more modules depend on each other, which can lead to import errors. Structure your code to avoid these.
- **Don’t over-nest subpackages**: Keep the directory structure shallow. Too many nested subpackages can lead to a more complicated codebase that’s harder to maintain.
- **Document each module**: Include a docstring at the beginning of each module or subpackage explaining its purpose and usage. This will help future developers (or your future self) understand the code quickly.

## Import Order

When writing imports statementsin, PEP8 recommends the following:

- Imports should be at the top of the file, after the module docstring.
- They should be divided in to the following groups in this order:
    1. **Standard Library Imports**: Begin by importing modules from the Python standard library. These are modules that come bundled with Python and do not require external installation.

    2. **Third-Party Library Imports**: Next, import modules from third-party libraries or packages installed via tools like pip.

    3. **Local Imports**: Finally, import modules from your own project or other local directories. These are modules that you have written yourself or are part of your project's structure.
- Each group of imports should be separated by a blank line.
- Within each group order your imports alphabetically.
