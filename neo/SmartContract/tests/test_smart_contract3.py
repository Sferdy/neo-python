import binascii
import os
from neo.Utils.BlockchainFixtureTestCase import BlockchainFixtureTestCase
from neo.IO.Helper import Helper
from neo.Core.Blockchain import Blockchain
from neo.Implementations.Blockchains.LevelDB.DBCollection import DBCollection
from neo.Implementations.Blockchains.LevelDB.DBPrefix import DBPrefix
from neo.Core.State.ContractState import ContractState
from neo.Core.State.AssetState import AssetState
from neocore.UInt256 import UInt256
from neocore.Cryptography.Crypto import Crypto
from neo.Settings import settings


class SmartContractTest3(BlockchainFixtureTestCase):

    @classmethod
    def leveldb_testpath(self):
        return os.path.join(settings.DATA_DIR_PATH, 'fixtures/test_chain')

    contract_create_block = b'00000000d22571288d1d2eb1088fca1a0d0af1a1019fe3d57470011c0c903d087c16ce7ced7b1633fb927096cc3de40cdc389f342a6b1346322eff316feba1a89763a49d565c575920550300bd61ebab4af00f4ef3812db982f3b0089a21a278988efeec6a027b2501fd4501405ae7a095f0ff12878a9dba20cf7448974c410832f5cc6eb4da2e91eef7de4c0159c15f2f4cdeec40003d82aa80789186fc50d18b8c63458200f4ed783757a1904029e48c992097fd07c5ce2f1544e8d80300e1b2e742cf5b24af2f4b5d8100fcab5c385e15dddd24856a2437b46f2ac09da8f2c87278afeea11eb5ac655b5f5d63404b65f93fb7de6659ef2956d4d50b430d950c010afb4762c0256f1982fc80220074c72e56403781209d4ad6d5accddd708c899e11e857e102b1d98796ff6d07584081dc4abaa4cf318b86137802cd0f175c4210a6e0199a7f94c16c585676aa09228a74617dacdd49e5335679180303fb944c39d1c44f0dd53225d3b53143c7c95d40f8d08b8c6a467f7f4d2f62d83cb70a5bf0cbbb7e8a74dd2c22af55432a1dd28f596be87adf3ca6b1b09a577215e09841319970747523e8510edb4efbcf795d65f155210209e7fd41dfb5c2f8dc72eb30358ac100ea8c72da18847befe06eade68cebfcb9210327da12b5c40200e9f65569476bbff2218da4f32548ff43b6387ec1416a231ee821034ff5ceeac41acf22cd5ed2da17a6df4dd8358fcb2bfb1a43208ad0feaab2746b21026ce35b29147ad09e4afe4ec4a7319095f08198fa8babbe3c56e970b143528d2221038dddc06ce687677a53d54f096d2591ba2302068cf123c1f2d75c2dddc542557921039dafd8571a641058ccc832c5e2111ea39b09c0bde36050914384f7a48bce9bf92102d02b1873a0863cd042cc717da31cea0d7cf9db32b74d4c72c01b0011503e2e2257ae020000bd61ebab00000000d101fdd90114746573742063726561746520636f6e74726163740c666c6f77406e656f2e6f726704666c6f7701310b74657374206372656174650002ff00004d810153c56b4ca4c56b6c766b00527ac46c766b51527ac46c766b52527ac461681e416e745368617265732e426c6f636b636861696e2e47657448656967687461681e416e745368617265732e426c6f636b636861696e2e4765744865616465726c766b53527ac46c766b00c36c766b53c361681d416e745368617265732e4865616465722e47657454696d657374616d70a163080000616c75666c766b51c36c766b52c3617cac616c75666c766b00527ac4030000006c766b52527ac46c766b52c30052c46c766b52c35156c46c766b52c36c766b51527ac461681e416e745368617265732e426c6f636b636861696e2e476574486569676874756c766b00c36c766b51c35100044c6f636b03312e3004464c4f570c464c4f57404e454f2e4f52470d4c6f636b20436f6e747261637461587951795a72755172755779527959727552727556795379587275537275557954795772755472756823416e745368617265732e426c6f636b636861696e2e437265617465436f6e747261637475616c75666819416e745368617265732e436f6e74726163742e43726561746500aaa0680b00000000019c7644365d4994899680ac10b58e06da00745948043ba5d448a1ecbd8ba94464010001e72d286979ee6cb1b7e65dfddfb2e384100b8d148e7758de42e4168b71792c60b1427ab0000000008e568bcbf3bab3d524f556a78148d462c0be7383014140defaa5df7b756acfbe1f639f300c8266ab10f04abaf5cda580b528114ecc3c30c493202595fa8e29b3542c73173b34c29bfd9b25ae126ef6d80624a3ee65464d2321039b2c6b8a8838595b8ebcc67bbc85cec78d805d56890e9a0d71bcae89664339d6ac'
    contract_hash = b'6c4d6f1c561a9d0a0af81cf28a5d70648c060f99'
    contract_block_index = 218400
    contract_block_script = b'53c56b4ca4c56b6c766b00527ac46c766b51527ac46c766b52527ac461681e416e745368617265732e426c6f636b636861696e2e47657448656967687461681e416e745368617265732e426c6f636b636861696e2e4765744865616465726c766b53527ac46c766b00c36c766b53c361681d416e745368617265732e4865616465722e47657454696d657374616d70a163080000616c75666c766b51c36c766b52c3617cac616c75666c766b00527ac4030000006c766b52527ac46c766b52c30052c46c766b52c35156c46c766b52c36c766b51527ac461681e416e745368617265732e426c6f636b636861696e2e476574486569676874756c766b00c36c766b51c35100044c6f636b03312e3004464c4f570c464c4f57404e454f2e4f52470d4c6f636b20436f6e747261637461587951795a72755172755779527959727552727556795379587275537275557954795772755472756823416e745368617265732e426c6f636b636861696e2e437265617465436f6e747261637475616c7566'

    def test_contract_create_block(self):

        hexdata = binascii.unhexlify(self.contract_create_block)

        block = Helper.AsSerializableWithType(hexdata, 'neo.Core.Block.Block')

        self.assertEqual(block.Index, self.contract_block_index)

        result = Blockchain.Default().Persist(block)

        self.assertTrue(result)

        snapshot = Blockchain.Default()._db.snapshot()

        contracts = DBCollection(Blockchain.Default()._db, snapshot, DBPrefix.ST_Contract, ContractState)

        contract_added = contracts.TryGet(self.contract_hash)

        self.assertIsNotNone(contract_added)

        self.assertEqual(contract_added.HasStorage, False)
        self.assertEqual(contract_added.Name, b'test create')
        self.assertEqual(contract_added.Email, b'flow@neo.org')

        self.assertEqual(len(Blockchain.Default().SearchContracts("test create")), 1)
        self.assertEqual(len(Blockchain.Default().SearchContracts("TEST CREate")), 1)
        self.assertEqual(len(Blockchain.Default().SearchContracts("TEST CREATE!")), 0)

        code = contract_added.Code

        self.assertIsNotNone(code)

        self.assertEqual(code.ReturnType, 255)

        self.assertEqual(code.ScriptHash().ToBytes(), self.contract_hash)
        self.assertEqual(code.Script.hex().encode('utf-8'), self.contract_block_script)

        snapshot.close()

    asset_create_block = b'000000004cb2a38f901afb2b85869161bd96f930babdbf65bd04c4842fe625ecc1a7a725e99a7bc87264d857405ebe90b88bfa5b279da7a92a32b0a3771ac560f1d0cc82e6ff5559b6420300a8a6a761b68e326df3812db982f3b0089a21a278988efeec6a027b2501fd4501408e6ceb56b2a98213e0027245920faa279f48b14279874634edd0ad2f06fc80a785545f6419f4400822b3f5f270e76b39718764a1476d95a1349e4f8398220ddf4091718c9eed0bd2faa38b964198787816b067a4d7268251b6bf348732e6848a2fc88cd7b17b55610586226584202a754196a9b70fde3936d9854fbc3724ce5a8940e16d39bf14a1313ddbc681f01e346386e23308e39074bd01e77ed5dc9196e6b6aa9806bd904d1d0d171edf6c563e4ad99dd5adbd64021c8c5e4c48a6b3aaeb4140e6482ec6c1bb8e21ec28b55bbb6ee8b34ced411f71bb25452bb68666c834b4a9d2cc152440720f9efb0e701024143d4a8fea7c985918048600ac44da0823f09240a6441778043e226d3e34e4e54b3c89e237ae8517034d131d4efc42b8eeb8f2a8a8f4fad014728ff3bf34782c3328146cda7a89bdc29d045ad28786c02c2a5af9f155210209e7fd41dfb5c2f8dc72eb30358ac100ea8c72da18847befe06eade68cebfcb9210327da12b5c40200e9f65569476bbff2218da4f32548ff43b6387ec1416a231ee821034ff5ceeac41acf22cd5ed2da17a6df4dd8358fcb2bfb1a43208ad0feaab2746b21026ce35b29147ad09e4afe4ec4a7319095f08198fa8babbe3c56e970b143528d2221038dddc06ce687677a53d54f096d2591ba2302068cf123c1f2d75c2dddc542557921039dafd8571a641058ccc832c5e2111ea39b09c0bde36050914384f7a48bce9bf92102d02b1873a0863cd042cc717da31cea0d7cf9db32b74d4c72c01b0011503e2e2257ae020000a8a6a76100000000d1019b1467f97110a66136d38badc7b9f88eab013027ce491467f97110a66136d38badc7b9f88eab013027ce4921034b44ed9c8a88fb2497b6b57206cc08edd42c5614bd1fee790e5b795dee0f4e11520500e40b54022d5b7b226c616e67223a227a682d434e222c226e616d65223a22476c6f62616c4173736574546573743032227d5d01606816416e745368617265732e41737365742e43726561746500beb72e74000000012067f97110a66136d38badc7b9f88eab013027ce49011421b58d4586c06887514f7e272b0851d83e3e7d99727a6cb2c738ffc25300d0000001e72d286979ee6cb1b7e65dfddfb2e384100b8d148e7758de42e4168b71792c6000d63d0e2c2f000067f97110a66136d38badc7b9f88eab013027ce490141403a06a71d5398b13adf03aa61f21820d48eca9ff312482284089504881995f606ec400da3fb36d9a307e44beb05b083c590a55b17272d0ca82d861d484063ef392321034b44ed9c8a88fb2497b6b57206cc08edd42c5614bd1fee790e5b795dee0f4e11ac'
    asset_create_index = 213686

    asset_create_id = b'f7c8f7bb9367bd5100c67c65522fb5ffb90fb7614d051f3cdc940da7298c995c'
    asset_admin = 'ARFe4mTKRTETerRoMsyzBXoPt2EKBvBXFX'

    def test_invocation_assetcreate_block(self):

        hexdata = binascii.unhexlify(self.asset_create_block)

        block = Helper.AsSerializableWithType(hexdata, 'neo.Core.Block.Block')

        self.assertEqual(block.Index, self.asset_create_index)

        result = Blockchain.Default().Persist(block)

        self.assertTrue(result)

        # now the asset that was created should be there
        sn = Blockchain.Default()._db.snapshot()
        assets = DBCollection(Blockchain.Default()._db, sn, DBPrefix.ST_Asset, AssetState)

        newasset = assets.TryGet(self.asset_create_id)

        self.assertIsNotNone(newasset)

        self.assertEqual(newasset.AssetType, 96)
        self.assertEqual(newasset.Precision, 2)
        self.assertEqual(Crypto.ToAddress(newasset.Admin), self.asset_admin)
        self.assertEqual(Crypto.ToAddress(newasset.Issuer), self.asset_admin)
        self.assertIsInstance(newasset.AssetId, UInt256)
        self.assertEqual(newasset.AssetId.ToBytes(), self.asset_create_id)
