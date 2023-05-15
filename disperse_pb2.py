# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disperse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64isperse.proto\x12\x0binterfaceDL\"I\n\x12\x45ncodeStoreRequest\x12\x10\n\x08\x44uration\x18\x01 \x01(\x04\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\x12\x13\n\x0b\x42lockNumber\x18\x03 \x01(\r\"\xc3\x02\n\x0bStoreParams\x12\x1c\n\x14ReferenceBlockNumber\x18\x0f \x01(\r\x12\x1b\n\x13TotalOperatorsIndex\x18\x10 \x01(\r\x12\x14\n\x0cOrigDataSize\x18\x01 \x01(\r\x12\x10\n\x08NumTotal\x18\x02 \x01(\r\x12\x0e\n\x06Quorum\x18\x03 \x01(\r\x12\x0e\n\x06NumSys\x18\x04 \x01(\r\x12\x0e\n\x06NumPar\x18\x05 \x01(\r\x12\x10\n\x08\x44uration\x18\x06 \x01(\r\x12\x11\n\tKzgCommit\x18\x07 \x01(\x0c\x12\x16\n\x0eLowDegreeProof\x18\x08 \x01(\x0c\x12\x0e\n\x06\x44\x65gree\x18\t \x01(\r\x12\x11\n\tTotalSize\x18\n \x01(\x04\x12\r\n\x05Order\x18\x0b \x03(\r\x12\x0b\n\x03\x46\x65\x65\x18\x0c \x01(\x0c\x12\x12\n\nHeaderHash\x18\r \x01(\x0c\x12\x11\n\tDisperser\x18\x0e \x01(\x0c\";\n\x10\x45ncodeStoreReply\x12\'\n\x05store\x18\x01 \x01(\x0b\x32\x18.interfaceDL.StoreParams\"?\n\x14\x44isperseStoreRequest\x12\x12\n\nHeaderHash\x18\x01 \x01(\x0c\x12\x13\n\x0bMessageHash\x18\x02 \x01(\x0c\"r\n\x12\x41ggregateSignature\x12\x0e\n\x06\x41ggSig\x18\x01 \x01(\x0c\x12\x19\n\x11StoredAggPubkeyG1\x18\x02 \x01(\x0c\x12\x17\n\x0fUsedAggPubkeyG2\x18\x03 \x01(\x0c\x12\x18\n\x10NonSignerPubkeys\x18\x04 \x03(\x0c\"n\n\x12\x44isperseStoreReply\x12-\n\x04sigs\x18\x01 \x01(\x0b\x32\x1f.interfaceDL.AggregateSignature\x12\x10\n\x08\x41pkIndex\x18\x02 \x01(\r\x12\x17\n\x0fTotalStakeIndex\x18\x03 \x01(\x04\"\x97\x01\n\x1b\x45ncodeAndDisperseStoreReply\x12\'\n\x05store\x18\x01 \x01(\x0b\x32\x18.interfaceDL.StoreParams\x12-\n\x04sigs\x18\x02 \x01(\x0b\x32\x1f.interfaceDL.AggregateSignature\x12\x0f\n\x07msgHash\x18\x03 \x01(\x0c\x12\x0f\n\x07storeId\x18\x04 \x01(\r\"3\n\x11StoreFrameRequest\x12\x0f\n\x07msgHash\x18\x01 \x01(\x0c\x12\r\n\x05\x66rame\x18\x03 \x01(\x0c\"4\n\x12StoreFramesRequest\x12\x0f\n\x07msgHash\x18\x01 \x01(\x0c\x12\r\n\x05\x66rame\x18\x03 \x03(\x0c\"$\n\x0fStoreFrameReply\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"&\n\x14RetrieveFrameRequest\x12\x0e\n\x06\x63ommit\x18\x01 \x01(\x0c\"#\n\x12RetrieveFrameReply\x12\r\n\x05\x66rame\x18\x01 \x01(\x0c\"8\n\x16\x43odingChallengeRequest\x12\x0e\n\x06\x63ommit\x18\x01 \x01(\x0c\x12\x0e\n\x06\x66rames\x18\x02 \x03(\x0c\"*\n\x17PaymentChallengeRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x9d\x01\n\x0e\x43hallengeReply\x12;\n\x06status\x18\x01 \x01(\x0e\x32+.interfaceDL.ChallengeReply.ChallengeStatus\x12\x11\n\tsignature\x18\x02 \x01(\x0c\";\n\x0f\x43hallengeStatus\x12\t\n\x05\x41GREE\x10\x00\x12\x0c\n\x08\x44ISAGREE\x10\x01\x12\x0f\n\x0bINTERNALERR\x10\x02\x32\xc5\x05\n\rDataDispersal\x12O\n\x0b\x45ncodeStore\x12\x1f.interfaceDL.EncodeStoreRequest\x1a\x1d.interfaceDL.EncodeStoreReply\"\x00\x12U\n\rDisperseStore\x12!.interfaceDL.DisperseStoreRequest\x1a\x1f.interfaceDL.DisperseStoreReply\"\x00\x12\x65\n\x16\x45ncodeAndDisperseStore\x12\x1f.interfaceDL.EncodeStoreRequest\x1a(.interfaceDL.EncodeAndDisperseStoreReply\"\x00\x12L\n\nStoreFrame\x12\x1e.interfaceDL.StoreFrameRequest\x1a\x1c.interfaceDL.StoreFrameReply\"\x00\x12N\n\x0bStoreFrames\x12\x1f.interfaceDL.StoreFramesRequest\x1a\x1c.interfaceDL.StoreFrameReply\"\x00\x12W\n\rRetrieveFrame\x12!.interfaceDL.RetrieveFrameRequest\x1a\x1f.interfaceDL.RetrieveFrameReply\"\x00\x30\x01\x12U\n\x0f\x43hallengeCoding\x12#.interfaceDL.CodingChallengeRequest\x1a\x1b.interfaceDL.ChallengeReply\"\x00\x12W\n\x10\x43hallengePayment\x12$.interfaceDL.PaymentChallengeRequest\x1a\x1b.interfaceDL.ChallengeReply\"\x00\x42=Z;github.com/Layr-Labs/datalayr/common/interfaces/interfaceDLb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'disperse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z;github.com/Layr-Labs/datalayr/common/interfaces/interfaceDL'
  _ENCODESTOREREQUEST._serialized_start=31
  _ENCODESTOREREQUEST._serialized_end=104
  _STOREPARAMS._serialized_start=107
  _STOREPARAMS._serialized_end=430
  _ENCODESTOREREPLY._serialized_start=432
  _ENCODESTOREREPLY._serialized_end=491
  _DISPERSESTOREREQUEST._serialized_start=493
  _DISPERSESTOREREQUEST._serialized_end=556
  _AGGREGATESIGNATURE._serialized_start=558
  _AGGREGATESIGNATURE._serialized_end=672
  _DISPERSESTOREREPLY._serialized_start=674
  _DISPERSESTOREREPLY._serialized_end=784
  _ENCODEANDDISPERSESTOREREPLY._serialized_start=787
  _ENCODEANDDISPERSESTOREREPLY._serialized_end=938
  _STOREFRAMEREQUEST._serialized_start=940
  _STOREFRAMEREQUEST._serialized_end=991
  _STOREFRAMESREQUEST._serialized_start=993
  _STOREFRAMESREQUEST._serialized_end=1045
  _STOREFRAMEREPLY._serialized_start=1047
  _STOREFRAMEREPLY._serialized_end=1083
  _RETRIEVEFRAMEREQUEST._serialized_start=1085
  _RETRIEVEFRAMEREQUEST._serialized_end=1123
  _RETRIEVEFRAMEREPLY._serialized_start=1125
  _RETRIEVEFRAMEREPLY._serialized_end=1160
  _CODINGCHALLENGEREQUEST._serialized_start=1162
  _CODINGCHALLENGEREQUEST._serialized_end=1218
  _PAYMENTCHALLENGEREQUEST._serialized_start=1220
  _PAYMENTCHALLENGEREQUEST._serialized_end=1262
  _CHALLENGEREPLY._serialized_start=1265
  _CHALLENGEREPLY._serialized_end=1422
  _CHALLENGEREPLY_CHALLENGESTATUS._serialized_start=1363
  _CHALLENGEREPLY_CHALLENGESTATUS._serialized_end=1422
  _DATADISPERSAL._serialized_start=1425
  _DATADISPERSAL._serialized_end=2134
# @@protoc_insertion_point(module_scope)