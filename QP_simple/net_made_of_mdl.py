#torch.nn.Moduleのサブクラスを定義する基本的な書き方は以下の通り
#1.__init__()で使用するmodule（layer）のインスタンスを生成する
#2.forward()で所望の順番で適用していく
#3.super().__init__()を忘れないように注意
