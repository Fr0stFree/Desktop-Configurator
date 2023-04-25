# <ct:object name="SH_ALL" access-level="public" access-scope="global" uuid="fab5def0-0776-4fb7-a4b4-ccf1d01a17f5">
#     <attribute type="unit.Server.Attributes.NodeRelativePath" />
#     <attribute type="unit.Server.Attributes.IsObject" value="false" />
#     <ct:object name="GP001" base-type="Types.FB_SH_ALL.FB_SH_ALL_PLC" access-level="public" access-scope="global" aspect="Aspects.PLC" uuid="14f9de14-87ec-4b5c-ae83-c192f9b60083">
#       <attribute type="unit.System.Attributes.Description" value="ГП 1. Здание входных ниток и пробкоуловителей" />
#       <attribute type="Attributes.GeneralPlan" value="ГП001" />
#     </ct:object>
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!НОВЫЙ ДАТЧИК! ОБЯЗАТЕЛЬНО ВСЁ ПРОВЕРИТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from core.validators import value_is_not_none_or_empty
from core.fields import Field, SeverityField
from core.sensors import Sensor

class FB_SH_ALL(Sensor):
  
    """
    Класс для работы с датчиками типа FB_SH_ALL. Поле Severity отсутствует в таблице, его значение
    рассчитывается на основе значения в поле SOUND_ON.
    """
    BASE_TYPE = 'Types.FB_SH_ALL.FB_SH_ALL_PLC'
    CLASS_NAME = 'SH_ALL'
    Name = Field(name='name', column='D', validators=[value_is_not_none_or_empty])
    Description = Field(name='Description', column='E', validators=[value_is_not_none_or_empty])
    GP = Field(name='GeneralPlan', column='J', validators=[value_is_not_none_or_empty])

    def to_omx(self) -> str:
        omx_block = (
            f'    <ct:object {self.Name.name}="{getattr(self, self.Name.key)}" base-type="{self.BASE_TYPE}" aspect="Aspects.PLC" access-level="public" uuid="{self.pk}">\n'
            f'      <attribute type="unit.System.Attributes.{self.Description.name}" value="{getattr(self, self.Description.key)}"/>\n'
            f'      <attribute type="Attributes.{self.GP.name}" value="{getattr(self, self.GP.key)}"/>\n'
            f'    </ct:object>\n'
        )
        return omx_block
