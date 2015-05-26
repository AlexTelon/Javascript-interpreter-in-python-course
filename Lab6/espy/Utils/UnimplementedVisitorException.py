import Utils

class UnimplementedVisitorException(BaseException):
  def __init__(self, ctx):
    super().__init__(Utils.prettyprintstr(ctx))