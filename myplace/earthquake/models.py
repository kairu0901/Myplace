from django.db import models
from base_app.models import BaseModel

class JapanEarthquakeRecord(BaseModel):
    monitoring_org = models.CharField(
        verbose_name="観測組織",
        max_length=1,
        choices=[
            ('J',' 気象庁による震源'),
            ('U','USGSが決定した震源'),
            ('I','その他の国際機関(ISC,IASPEIなど)による震源'),
        ]
    )
    monitoring_datetime = models.DateTimeField(
        verbose_name='観測日時',
    )
    standard_error_second = models.CharField(
        verbose_name='オリジンタイムの標準誤差(秒)',
        max_length=4
    )
from django.db import models
from decimal import Decimal
from datetime import datetime, timezone


# --- コード選択肢（choices） ---

class RecordType(models.TextChoices):
    JMA = 'J', '気象庁'
    USGS = 'U', 'USGS'
    INTL = 'I', '国際機関(ISC 等)'


class MagnitudeType(models.TextChoices):
    J = 'J', '坪井変位'
    D = 'D', '坪井変位準拠'
    d = 'd', '坪井変位準拠(2点)'
    V = 'V', '速度マグニチュード'
    v = 'v', '速度(2–3点)'
    W = 'W', 'モーメント(Mw)'
    B = 'B', '実体波(Mb)'
    S = 'S', '表面波(Ms)'
    BLANK = ' ', '欠損'


class TravelTimeTable(models.TextChoices):
    T1 = '1', 'T1 系'
    T2 = '2', 'T2 系'
    T3 = '3', 'T3 系'
    T4 = '4', 'T4 系'
    T5 = '5', 'JMA2001'
    T6 = '6', 'JMA2001+LL'
    T7 = '7', 'JMA2001A/2020 系'
    BLANK = ' ', '欠損'


class SourceEval(models.TextChoices):
    DEPTH_FREE = '1', '深さフリー'
    DEPTH_STEP = '2', '深さ刻み'
    FIXED_OR_MANUAL = '3', '深さ固定/人的判断'
    DEPTH_PHASE = '4', 'Depth Phase'
    SP = '5', 'S-P使用'
    REF_OLD = '7', '参考'
    IMPOSSIBLE = '8', '決定不能'
    FIXED_HYPO = '9', '震源固定'
    MATCHED_FILTER = 'M', 'Matched Filter'
    BLANK = ' ', '欠損'


class JMAExtraInfo(models.TextChoices):
    NORMAL = '1', '通常地震'
    DEP_ON_OTHERS = '2', '他機関依存'
    ARTIFICIAL = '3', '人工地震'
    VOLC_EQ = '4', '火山性イベント'
    LOW_FREQ = '5', '低周波'
    BLANK = ' ', '欠損'


class MaxIntensity(models.TextChoices):
    I1 = '1', '震度1'
    I2 = '2', '震度2'
    I3 = '3', '震度3'
    I4 = '4', '震度4'
    I5W_OLD = '5', '震度5(旧)'
    I6_OLD = '6', '震度6(旧)'
    I7 = '7', '震度7'
    I5L = 'A', '震度5弱'
    I5U = 'B', '震度5強'
    I6L = 'C', '震度6弱'
    I6U = 'D', '震度6強'
    LOCAL = 'L', '局発'
    SMALL_LOCAL = 'S', '小局発'
    SOMEWHAT = 'M', 'やや顕著'
    REMARKABLE = 'R', '顕著'
    FELT_OLD = 'F', '有感(旧)'
    NEAR_FELT = 'X', '付近有感(旧)'


class DamageScale(models.TextChoices):
    D1 = '1', '微小被害'
    D2 = '2', '小被害'
    D3 = '3', '大被害'
    D4 = '4', '甚大被害'
    D5 = '5', '壊滅的被害'
    D6 = '6', '広域甚大'
    D7 = '7', '壊滅(広域)'
    X = 'X', '被害不明(旧)'
    Y = 'Y', '合算被害(旧)'


class TsunamiScale(models.TextChoices):
    TS_OBS_NO_DAMAGE = '1', '観測のみ(被害なし)'
    T = 'T', '津波あり'
    H50 = '1', '〜0.5m'
    H1M = '2', '〜1m'
    H2M = '3', '〜2m'
    H4_6M = '4', '〜4–6m'
    H10_20M = '5', '〜10–20m'
    H30M_PLUS = '6', '30m以上'


class HypoFlag(models.TextChoices):
    K = 'K', '気象庁震源'
    S = 'S', '参考震源'
    k = 'k', '簡易震源'
    s = 's', '簡易参考'
    A = 'A', '自動震源'
    a = 'a', '自動参考'
    N = 'N', '未計算'
    F = 'F', '遠地'


# --- 震源レコード ---

class HypocenterRecord(BaseModel):
    """気象庁・震源レコード（固定長フォーマット準拠）"""

    # 基本
    record_type = models.CharField(
        verbose_name='レコード種別',
        max_length=1,
        choices=RecordType.choices,
    )
    origin_year = models.IntegerField(
        verbose_name='発震年',
    )
    origin_month = models.IntegerField(
        verbose_name='発震月',
    )
    origin_day = models.IntegerField(
        verbose_name='発震日',
    )
    origin_hour = models.IntegerField(
        verbose_name='発震時',
    )
    origin_minute = models.IntegerField(
        verbose_name='発震分',
    )
    origin_second = models.DecimalField(
        verbose_name='発震秒',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    origin_std_err_sec = models.DecimalField(
        verbose_name='発震時刻標準誤差(秒)',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # 震央（緯度経度）
    lat_deg = models.IntegerField(
        verbose_name='緯度(度)',
        null=True,
        blank=True,
    )
    lat_min = models.DecimalField(
        verbose_name='緯度(分)',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    lat_std_err_min = models.DecimalField(
        verbose_name='緯度標準誤差(分)',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    lon_deg = models.IntegerField(
        verbose_name='経度(度)',
        null=True,
        blank=True,
    )
    lon_min = models.DecimalField(
        verbose_name='経度(分)',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    lon_std_err_min = models.DecimalField(
        verbose_name='経度標準誤差(分)',
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # 深さ
    depth_km = models.DecimalField(
        verbose_name='深さ(km)',
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    depth_std_err_km = models.DecimalField(
        verbose_name='深さ標準誤差(km)',
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # マグニチュード
    mag1 = models.DecimalField(
        verbose_name='マグニチュード1',
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
    )
    mag1_type = models.CharField(
        verbose_name='M1種別',
        max_length=1,
        choices=MagnitudeType.choices,
        null=True,
        blank=True,
    )
    mag2 = models.DecimalField(
        verbose_name='マグニチュード2',
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
    )
    mag2_type = models.CharField(
        verbose_name='M2種別',
        max_length=1,
        choices=MagnitudeType.choices,
        null=True,
        blank=True,
    )

    # コード類
    travel_time_table = models.CharField(
        verbose_name='走時表',
        max_length=1,
        choices=TravelTimeTable.choices,
        null=True,
        blank=True,
    )
    source_eval = models.CharField(
        verbose_name='決定手法',
        max_length=1,
        choices=SourceEval.choices,
        null=True,
        blank=True,
    )
    jma_extra_info = models.CharField(
        verbose_name='補助情報',
        max_length=1,
        choices=JMAExtraInfo.choices,
        null=True,
        blank=True,
    )
    max_intensity = models.CharField(
        verbose_name='最大震度',
        max_length=1,
        choices=MaxIntensity.choices,
        null=True,
        blank=True,
    )
    damage_scale = models.CharField(
        verbose_name='被害規模',
        max_length=1,
        choices=DamageScale.choices,
        null=True,
        blank=True,
    )
    tsunami_scale = models.CharField(
        verbose_name='津波規模',
        max_length=1,
        choices=TsunamiScale.choices,
        null=True,
        blank=True,
    )

    # 地域・名称
    region_large_code = models.IntegerField(
        verbose_name='地域コード(大)',
        null=True,
        blank=True,
    )
    region_small_code = models.IntegerField(
        verbose_name='地域コード(小)',
        null=True,
        blank=True,
    )
    epicenter_name = models.CharField(
        verbose_name='震央地名',
        max_length=24,
        null=True,
        blank=True,
    )

    # その他
    station_count = models.IntegerField(
        verbose_name='観測点数',
        null=True,
        blank=True,
    )
    hypo_flag = models.CharField(
        verbose_name='震源フラグ',
        max_length=1,
        choices=HypoFlag.choices,
        null=True,
        blank=True,
    )

    # 監査用（固定長原文）
    raw_line = models.CharField(
        verbose_name='固定長レコード原文',
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = '震源レコード'
        verbose_name_plural = '震源レコード'
        indexes = [
            models.Index(fields=['origin_year', 'origin_month', 'origin_day']),
            models.Index(fields=['region_large_code', 'region_small_code']),
            models.Index(fields=['mag1']),
            models.Index(fields=['hypo_flag']),
        ]

    # --- 便利プロパティ ---

    @property
    def origin_datetime(self):
        """origin_* をUTCの datetime に組み立て"""
        try:
            sec = self.origin_second or Decimal('0')
            whole = int(sec)
            micro = int((sec - whole) * Decimal('1000000'))
            return datetime(
                self.origin_year, self.origin_month, self.origin_day,
                self.origin_hour, self.origin_minute, whole, micro,
                tzinfo=timezone.utc
            )
        except Exception:
            return None

    @property
    def latitude_decimal(self):
        """緯度を10進度へ（北緯前提）"""
        if self.lat_deg is None or self.lat_min is None:
            return None
        return Decimal(self.lat_deg) + (self.lat_min / Decimal('60'))

    @property
    def longitude_decimal(self):
        """経度を10進度へ（東経前提）"""
        if self.lon_deg is None or self.lon_min is None:
            return None
        return Decimal(self.lon_deg) + (self.lon_min / Decimal('60'))

    def __str__(self):
        dt = self.origin_datetime
        dt_s = dt.isoformat() if dt else 'unknown'
        return f'{dt_s} M{self.mag1 or ""} {self.epicenter_name or ""}'
