# {tm.name}

## System Description

{tm.description}

## Dataflow Diagram - Level 0 DFD

![](sample.png)

&nbsp;

## Dataflows

Name|From|To |Data|Protocol|Port
|:----:|:----:|:---:|:----:|:--------:|:----:|
{dataflows:repeat:|{{item.display_name:call:}}|{{item.source.name}}|{{item.sink.name}}|{{item.data}}|{{item.protocol}}|{{item.dstPort}}|
}

## Data Dictionary

Name|Description|Classification|Carried|Processed
|:----:|:--------:|:----:|:----|:----|
{data:repeat:|{{item.name}}|{{item.description}}|{{item.classification.name}}|{{item.carriedBy:repeat:{{{{item.name}}}}<br>}}|{{item.processedBy:repeat:{{{{item.name}}}}<br>}}|
}

## Actors

{actors:repeat:
Name|{{item.name}}
|:----|:----|
Description|{{item.description}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

### Threats

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &emsp;
</details>
}}
}}
}

## Assets

{assets:repeat:
Name|{{item.name}}|
|:----|:----|
Description|{{item.description}}|
In Scope|{{item.inScope}}|
Type|{{item:call:getElementType}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

## Threats

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &nbsp;
</details>
}}
}}
}

## Data Flows

{dataflows:repeat:
Name|{{item.name}}
|:----|:----|
Description|{{item.description}}|
Sink|{{item.sink}}|
Source|{{item.source}}|
Is Response|{{item.isResponse}}|
In Scope|{{item.inScope}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

### Threats

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &emsp;
</details>
}}
}}
}