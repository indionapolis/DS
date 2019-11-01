## Before

### Screenshot
![](src/before.png)

### rs.status()
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T08:50:26.016Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572598224, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T08:50:24.469Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572598224, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T08:50:24.469Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572598224, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572598224, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T08:50:24.469Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T08:50:24.469Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572598164, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572598164, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-11-01T07:13:23.476Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572592393, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T07:13:24.284Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T07:13:24.962Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "machine1:27017",
			"ip" : "172.31.19.52",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 5899,
			"optime" : {
				"ts" : Timestamp(1572598224, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T08:50:24Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572592403, 1),
			"electionDate" : ISODate("2019-11-01T07:13:23Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "machine2:27017",
			"ip" : "172.31.30.209",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 5832,
			"optime" : {
				"ts" : Timestamp(1572598224, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572598224, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T08:50:24Z"),
			"optimeDurableDate" : ISODate("2019-11-01T08:50:24Z"),
			"lastHeartbeat" : ISODate("2019-11-01T08:50:24.952Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T08:50:24.950Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "machine1:27017",
			"syncSourceHost" : "machine1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "machine3:27017",
			"ip" : "172.31.19.39",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 5832,
			"optime" : {
				"ts" : Timestamp(1572598224, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572598224, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T08:50:24Z"),
			"optimeDurableDate" : ISODate("2019-11-01T08:50:24Z"),
			"lastHeartbeat" : ISODate("2019-11-01T08:50:24.952Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T08:50:24.950Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "machine1:27017",
			"syncSourceHost" : "machine1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572598224, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572598224, 1)
}
```

### rs.config()

```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "machine1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "machine2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "machine3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbbdb098614c89203119d8e")
	}
}
```

## After

### Screenshot
![](src/after.png)

### rs.status()

```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T08:57:01.631Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572598613, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T08:56:53.496Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572598613, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T08:56:53.496Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572598613, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572598613, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T08:56:53.496Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T08:56:53.496Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572598583, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572598583, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-11-01T08:54:52.494Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572598484, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572598484, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T08:54:53.492Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T08:54:54.222Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "machine1:27017",
			"ip" : "172.31.19.52",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T08:56:53.354Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T08:54:53.020Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to machine1:27017 (172.31.19.52:27017) :: caused by :: No route to host",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "machine2:27017",
			"ip" : "172.31.30.209",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 6293,
			"optime" : {
				"ts" : Timestamp(1572598613, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T08:56:53Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572598492, 1),
			"electionDate" : ISODate("2019-11-01T08:54:52Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "machine3:27017",
			"ip" : "172.31.19.39",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 6227,
			"optime" : {
				"ts" : Timestamp(1572598613, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572598613, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T08:56:53Z"),
			"optimeDurableDate" : ISODate("2019-11-01T08:56:53Z"),
			"lastHeartbeat" : ISODate("2019-11-01T08:57:00.512Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T08:57:00.245Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "machine2:27017",
			"syncSourceHost" : "machine2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572598613, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572598613, 1)
}
```

### rs.config()

```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "machine1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "machine2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "machine3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbbdb098614c89203119d8e")
	}
}
```