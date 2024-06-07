from enum import Enum

class ActorType(str, Enum):
	PERSON = 'Person',
	GROUP = 'Group'


class RelationType(str, Enum):
	FRIENDSHIP = 'Friendship',
	INVITED = 'Invited',
	BLOCK = 'Block'

