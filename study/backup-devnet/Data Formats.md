## JSON

Uses curley brackets to enclose the object.  Uses key:value pairs.  Values can be objects, arrays, or array of objects

```json
{
	"employees": [
		{"firstName":"John", "lastName":"Smith"}
	]
}
```

- Commenting is not allowed
- Whitespace has no impact
- Case-sensitive
- Generally considered easier to interpret and write
- No end tags
- JSON easier to parse than XML

## XML
XML is a language to store & describe data.  It does not actually perform any operations.  XML uses a tree structure, and the tagged items are called elements (similar to HTML)

- Any word can be used for element tags (except for XML)
- Element tags are case sensitive
- No spaces are allowed
	- Use underscores or hyphens to separate words
- Element tags must start with either underscore or a letter
- Can add comments to XML

## YAML
- Contains data arranged in hierarchical format.
- Considered one of the most human-readable formats.
- Key:value pairs for differentiating data
`
```yaml
nodes:
	- id: n1
		label: SW1
		node_definition: iosv12
		configuration: null
		interfaces:
			id: 11
			slot: 1
			label: GigabitEthernet0/1
			type: physical
	- id: n2
		label: R1
		node:definition: iosv
		configuration: | -
			Building Configuration...
		Current configuration : 1361 bytes
		!
		! Last configuration change at 14:21:40

```

- Able to interact with JSON
- Case Sensitive
- Whitespace is critical
- Lightweight and easy to create or modify
- Very human-readable
- Appropriate for configuration settings
- Whitespace considerations can make reading difficult
	- Can appear as a giant wall of text
- Errors can be ambiguous
- Used by Cisco Modeling Labs (CML) for importing/exporting lab files