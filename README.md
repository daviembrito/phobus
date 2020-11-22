# **Phobus**
Python program for parsing html href's by url

## **Installation**
git clone https://github.com/DearFuture1/phobus

## **Usage**
```python3 phobus.py [-h] [-a] [-o OUTPUT] [-i] [-f FILTER] url```

### **Arguments**
<p>
    <table>
        <thead>
            <tr>
                <th>Args</th>
                <th>Default</th>
                <th>Required</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>url</td>
                <td>None</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>-a, -all</td>
                <td>False</td>
                <td>No</td>
            </tr>
            <tr>
                <td>-o, --output</td>
                <td>None</td>
                <td>No</td>
            </tr>
            <tr>
                <td>-i, --ip</td>
                <td>False</td>
                <td>No</td>
            </tr>
            <tr>
                <td>-f, --filter</td>
                <td>http, https</td>
                <td>No</td>
            </tr>
        </tbody>
    </table>
</p>
<p></p>

### **-a, --all**

Show all the results without any filter

### **-o ```<```file```>```, --output ```<```file**```>```

Saves the output into a file

### **-i, --ip**

Tries to resolve all the adresses and get their ip's

### **-f ```<```filter```>```, --filter ```<```filter**```>```

Custom filter to href's
<p></p>

## **Examples**
<p></p>

![Default example](https://media.discordapp.net/attachments/352864897979121664/779902583736107039/default.PNG?width=797&height=172)

![Ip's](https://cdn.discordapp.com/attachments/352864897979121664/779902793875324938/allips.PNG)

![Custom filter](https://cdn.discordapp.com/attachments/352864897979121664/779902810467860480/customfilter.PNG)

![All flags](https://cdn.discordapp.com/attachments/352864897979121664/779902824594276352/every.PNG)

