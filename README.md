# **Phobus**
Python command line program for parsing HTML href's by url

## **Installation**
git clone https://github.com/DearFuture1/phobus.git

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

Tries to resolve all the addresses and get their ip's

### **-f ```<```filter```>```, --filter ```<```filter**```>```

Custom filter to href's
<p></p>

## **Examples**
<p></p>

![Default example](https://cdn.discordapp.com/attachments/711704296692908142/779910060327436298/default1.png)

![Ip's](https://cdn.discordapp.com/attachments/711704296692908142/779910078492966972/allips1.png)

![Custom filter](https://cdn.discordapp.com/attachments/711704296692908142/779910099786399774/customfilter1.png)

![All flags](https://cdn.discordapp.com/attachments/711704296692908142/779910117029576704/every1.png)

