# JSON Substitution Script
This script performs a substitution on a JSON file, replacing all non-dictionary values with a dictionary containing the original value and its type. The substitution is performed recursively to a specified depth.

## Usage
To use the script, run the following command in a terminal:

```python substitute.py input.json --depth [depth] output.json```

Replace input.json and output.json with the input and output file paths, respectively. The --depth flag is optional and specifies the maximum depth to perform substitution. If not specified, substitution is performed to the full depth.

## Example
For example, suppose we have the following input JSON file input.json:

```
{
    "name": "Muhammad Ali",
    "age": 26,
    "isMarried": true,
    "hobbies": ["reading", "swimming", "coding"],
    "address": {
        "street": "12 Abc Main St",
        "city": "Lahore",
        "state": "Punjab",
        "zip": "12345"
    }
}
```
To perform the substitution with a maximum depth of 2, run the following command:


```
python substitute.py input.json output.json --depth 2
```
This produces the following output JSON file output.json:

```
{
  "name": {
    "_content": "Muhammad Ali",
    "_type": "<class 'str'>"
  },
  "age": {
    "_content": 26,
    "_type": "<class 'int'>"
  },
  "isMarried": {
    "_content": true,
    "_type": "<class 'bool'>"
  },
  "hobbies": {
    "_content": [
      "reading",
      "swimming",
      "coding"
    ],
    "_type": "<class 'list'>"
  },
  "address": {
    "street": {
      "_content": "12 Abc Main St",
      "_type": "<class 'str'>"
    },
    "city": {
      "_content": "Lahore",
      "_type": "<class 'str'>"
    },
    "state": {
      "_content": "Punjab",
      "_type": "<class 'str'>"
    },
    "zip": {
      "_content": "12345",
      "_type": "<class 'str'>"
    }
  }
}
```
As we can see, all non-dictionary values have been replaced with a dictionary containing the original value and its type. The substitution has been performed to a depth of 2 on the address dictionary.
