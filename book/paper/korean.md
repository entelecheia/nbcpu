IV. 토픽모형을 활용한 캄보디아 중앙은행 정책 불확실성 측정

1. 개요

캄보디아는 달러라이제이션(dollarization) 기반의 경제로, 독립적인 통화 정책을 시행하는 데 한계를 가지고 있다. 2000년대에 국가 통화인 리엘(Riel)의 성장과 확장에도 불구하고, 캄보디아 중앙은행(National Bank of Cambodia, NBC)은 금융시장의 양적 및 질적 성숙도가 아직은 발전도상에 있는 상황으로 커뮤니케이션 피드백 경로가 미흡한 실정이다. 이러한 현대 통화 정책 전달 경로의 미비는 통화 정책을 관리하는 데 있어 제약 사항이 되고 있다.
전통적인 시장 메커니즘이 미발달한 환경에서는 적절한 비전통적 통화 정책 의사소통 도구와 전략을 구축하는 것이 시급하다. 이러한 필요성은 캄보디아의 경제 상황에서 특히 강조되는데, 통화의 디달러라이제이션(dedollarization)과 통화 정책 시행의 현대화 과정이 정책 불확실성을 초래할 수 있기 때문이다. 이러한 불확실성을 최소화하는 것은 경제의 안정성과 예측 가능성을 위해 매우 중요하다.
따라서 중앙은행의 정책 불확실성을 측정하는 것은 캄보디아 경제와 금융시장에 대한 통화정책의 영향을 이해하고 관리하는 데 중요한 과제이다. 또한 중앙은행이 대중과 금융시장에 정책 입장을 명확하게 전달하고 투명성과 신뢰를 높이는 데에도 중요한 영향을 미친다.
토픽(주제) 기반의 서술적 접근법은 이러한 상황에서 캄보디아의 중앙은행 정책 불확실성을 측정하는 데 특히 적합하다고 판단된다. 따라서, 본 연구에서는 텍스트 기반 토픽모형(Topic Model)을 사용하여 불확실성을 평가함으로 통화 정책, 통화 안정화 노력, 디달러라이제이션(dedollarization) 정책과 관련된 불확실성의 근본적 원인을 파악하고자 한다.
캄보디아의 달러라이제이션(dollarization) 경제 환경에서 통화 정책은 환율 관리가 가장 큰 정책수단이다. 이러한 상황에서의 불확실성은 통화 관리 정책의 잠재적 변화 가능성과 경제에 대한 사후적 영향을 포함한다고 할 수 있다. 따라서, 정책 불확실성을 측정하고 이해하는 데에는 다면적 접근법이 중요하다고 할 수 있으며, 본 연구는 토픽(주제) 기반 방법의 적용과 평가를 통해 이러한 문제을 해결하려고 한다. 이 연구의 결과는 별도의 파이썬 라이브러리와 보충자료로 제공되어, 캄보디아 국립은행(NBC)이 향후 정책 불확실성을 측정하는 데 바로 활용할 수 있을 것으로 기대된다.

1. 연구동향

경제 정책 불확실성에 대한 연구는 금융시장, 경제 성과, 기업 투자, 노동시장 역동성, 정치 양극화 등 광범위한 범위에 걸쳐 있으며 최근 연구의 중요한 주제중 하나이다. 불확실성을 측정하는 방법에는 크게 금융 데이터 기반 접근법과 텍스트 기반 접근법이 있다. 실시간, 보편적으로 적용 가능한 불확실성 측정 방법에 대한 연구는 지속적으로 진행되고 있다.

가. 금융데이터 기반 접근법

금융데이터 기반 측정 방식은 주로 주식시장의 변동성을 사용하는 방식과 예상치와 실제 금융 지표 간의 차이를 활용하는 방식으로 나뉜다. VIX 지수가 전자의 대표적인 예이다. VIX 지수는 미국 주식시장의 변동성을 측정하는 지표로, 주식시장의 변동성이 높을수록 불확실성이 높다고 판단한다. 후자의 대표적인 예로는 주식시장의 서프라이즈, 설문 조사를 통해 수집된 예상 및 실제 거시 경제 지표 간의 차이 등이 있다(Kaveh-yazdy와 Zarifzadeh, 2021). 이러한 방법은 불확실성을 평가하기 위한 정량적인 방법을 제공하며, 이를 직접 관찰 가능한 금융시장 움직임과 연결하게 만들어 주는 장점이 있다.

나. 텍스트 기반 접근법

텍스트 기반 접근법은 금융데이터의 정량적 분석 방식에서 통화 정책 문서, 소셜 미디어 게시물, 뉴스 기사와 같은 문서의 질적 분석으로의 전환을 의미한다. Baker et al. (2016)이 제안한 경제 정책 불확실성(EPU) 지수가 대표적인 예이다. EPU 지수는 텍스트 기반 접근법의 대표적인 지표로, 특정 불확실성 관련 키워드를 포함하는 기사의 빈도를 측정함으로써, 경제 정책 불확실성을 정량화한다. 하지만, 이 방법은 텍스트의 내용을 고려하지 않고, 특정 키워드의 빈도만을 고려하기 때문에, 불확실성의 다양한 유형을 구별할 수 없다는 단점이 있다. 또한, EPU 지수는 검증과정에서 노동 집약적 수작업 방식을 사용하는 문제가 있다. 이러한 단점을 보완하기 위해, 최근에는 토픽모형을 활용한 텍스트 기반 접근법이 제안되고 있다. 이 방법은 텍스트의 내용을 고려하여 불확실성의 다양한 유형을 구별할 수 있으며, 불확실성을 측정하기 위한 정량적 방법을 제공한다는 장점이 있다. Azqueta-Gavaldón (2017)는 불확실성 측정을 위해 토픽모형의 하나인 잠재 디리클레 할당(LDA)의 사용하였다. Kaveh-yazdy와 Zarifzadeh (2021)의 연구는 정확한 문서 분류와 태깅을 위해 서포트 벡터 머신과 로지스틱 회귀와 같은 기계학습 기술을 사용하였다.
텍스트 기반 접근법 중 특히 토픽 기반 접근법은 비지도학습 방식의 특성으로 인해 다양한 연구에 확대 적용 되었다. Larsen(2021)는 사전 훈련이나 라벨링 없이 기사를 내용과 주제를 기반으로 분류하기 위해 토픽모형(LDA)을 활용하고 있다. 이 방법은 기사의 전체 단어 구성(Mixture)이 토픽(주제)를 식별하여 다양한 유형의 불확실성을 구별하고 더 섬세한 이해를 제공하는 데 도움이 된다.
비정량 데이터 기반 불확실성 측정 방법은 지속적으로 발전하고 있다. 143개 국가를 포함하는 세계 불확실성 지수(WUI)로 확장되었으며, 의미 클러스터링, 단어 임베딩, 퍼지 k-평균을 사용하는 새로운 접근법으로 실시간 측정 및 지수 업데이트가 용이하게 되었다(Miranda-belmonteet 등, 2023).

1. 데이터

본 연구에 사용할 데이터는 캄보디아의 두 주요 뉴스 매체에서 기사를 수집, 필터링 및 분석하는 과정을 통해 확보하였다. 이 절에서는 데이터 소스와 수집 과정에 대해 설명한다.

가. 데이터 소스

데이터 소스로는 캄보디아의 두 주요 영문 뉴스 매체인 Khmer Times와 Phnom Penh Post에서 기사를 사용한다. 이 두 뉴스 매체는 캄보디아의 경제 및 금융 문제, 통화 정책을 포함하여 광범위하게 다루고 있어 선택되었다.

(가) Khmer Times

Khmer Times는 캄보디아의 주요 영어 신문으로, 국내 및 국제 사안, 정치, 비즈니스, 라이프스타일, 문화 등 다양한 뉴스를 제공한다. 다양한 분야의 기사는 캄보디아의 경제 및 금융 문제에 대한 귀중한 자료가 된다.

(나) Phnom Penh Post

Phnom Penh Post는 캄보디아에서 가장 오래된 독립 신문으로 알려져 있으며, 정치, 경제, 라이프스타일, 문화 등 다양한 주제에 대한 상세한 보도를 제공한다. 신문의 국내 경제 문제와 정책에 대한 심층 분석은 Kmer Times를 보완할 것으로 기대된다.

나. 데이터 수집

데이터 수집 과정은 관련 기사를 수집, 필터링 및 분석하여 충분한 기간의 데이터셋을 구축하는 데 목적이 있다.

(가) 웹 스크래핑

웹 스크래핑은 웹 상의 데이터를 추출하는 자동화된 프로세스이다. 본 연구에서는 `BeautifulSoup`과 `requests`와 같은 Python 라이브러리를 활용하여 Khmer Times와 Phnom Penh Post의 웹사이트에서 기사를 수집한다. 스크래핑 과정은 각 기사의 헤드라인, 날짜, 전체 텍스트를 포함한 필수 세부 정보를 추출한다.

(나) 키워드 필터링

본 연구에서는 "캄보디아 중앙은행," "통화 정책," "환율" 등과 같은 경제 정책과 관련된 특정 키워드와 "불확실성," "위험," "불확실" 등과 같은 불확실성과 관련된 키워드를 사용하여 필터링 하였다. 이러한 키워드는 캄보디아의 경제 정책과 관련된 기사를 포함하고 있으며, 이는 캄보디아의 경제 정책 불확실성을 평가하는 데 필요한 정보를 제공한다.

(다) 기간

데이터셋의 기가은 2014년 1월 1일부터 2023년 7월 31일까지의 약 10년에 걸친 기사를 포함한다. 이 기간은 캄보디아의 경제 정책 불확실성을 평가하는 데 충분한 기간을 제공한다.

나. 탐색적 데이터 분석

수집한 전체 데이터셋을 탐색적 데이터 분석(EDA)을 통해 데이터셋의 특성을 파악하였다. EDA는 데이터셋의 특성을 파악하고, 데이터셋의 품질을 평가하는 데 도움이 된다. 이 절에서는 데이터셋의 연간 분포, 전반적인 추세를 파악하기 위해 EDA를 수행하였다. 수집된 전체 기사는 총 40,002개이며, 전처리 후 최종 데이터셋은 39,632개의 기사로 구성되었다.

데이터셋의 연간 분포는 다음의 패턴을 보이고 있다. 시작연도인 2014년에는 총 2,047개의 기사가 있으며 평균 3,345단어를 가지고 있다 2015년에서 2018년 사이에는 기사의 양이 안정적으로 증가하여 2018년에 3,530개로 정점에 이르며, 평균 길이는 3,162에서 3,486단어 사이로 나타난다. 2019년에서 2020년 사이에는 기사의 양이 지속적인 확장하는 가운데 2020년에 4,688개의 기사로 정점에 이르며, 평균 길이는 약 3,400단어를 유지한다. 2021년과 2022년에는 기사가 뚜렷한 급증을 나타내어 연속 두 해에 각각 5,493개와 6,866개의 기사가 존재한다. 평균 길이는 약 3,100단어로 약간 감소한다. 2023년에는 약 7개월 동안 3,750개의 기사가 있으며 기사는 평균 3,255단어를 가지고 있다. <그림 3-1>은 기사 수의 지속적인 증가를 보여주고 있으며, 평균 길이는 약간의 변동에도 불구하고, 전체적으로 3,247단어로 상대적으로 안정적이다.

<그림 3-1>
기사수의 변화

1. 방법론

가. 개요

중앙은행 정책 불확실성을 측정하는 것은 금리 변동, 지급준비금 요구사항 또는 기타 통화 정책 도구와 같은 중앙은행이 취한 통화 정책 결정과 관련된 불확실성을 평가하는 것을 포함한다. 이에는 몇 가지 일반적인 접근 방식이 있다. 이 절에서는 텍스트 기반 접근법의 토픽 기반 방법을 사용하여 캄보디아의 중앙은행 정책 불확실성을 측정하는 방법을 제안한다. 이 접근법은 텍스트의 내용을 고려하여 불확실성의 다양한 유형을 구별할 수 있으며, 불확실성을 측정하기 위한 정량적 방법을 제공한다는 장점이 있다.

1. 중앙은행 커뮤니케이션 텍스트 분석: 이 방법은 중앙은행이 한 커뮤니케이션, 회의록, 연설, 보고서, 보도 자료 및 기타 커뮤니케이션 형태를 분석하는 것을 포함한다. 텍스트 내용은 수동으로 분석하거나 자연어처리(NLP, Natural Language Processing) 기술을 사용하여 분석할 수 있다. 불확실성과 관련된 키워드를 찾거나 불확실성 수준을 정량화하기 위해 토픽(주제) 모델링 또는 감정 분석과 같은 보다 정교한 기술을 사용할 수 있다. 예를 들어, Baker et al. (2016)의 EPU 지수가 이 방법의 대표적인 예이다. 한국은행 통화화정책 어조를 분석한 Lee et al. (2019a,b)의 연구도 이 방법의 대표적인 예이다.

2. 금융시장 데이터 기반 측정: 이 방법은 금융시장 데이터를 사용하여 정책 불확실성 수준을 추정한다. 가정은 금융시장이 미래 통화 정책에 대한 지각된 불확실성을 포함한 모든 가능한 정보를 포함하고 있다는 것이다. 이러한 방식의 예로는 VIX 지수와 같은 옵션 내재변동성 측정이 있으며, 이는 시장의 미래 변동성에 대한 기대를 포착한다. 또 다른 예로는 미국 국채 시장의 변동성을 측정하는 MOVE 지수가 있다. 이러한 지표는 불확실성의 대용치로 사용될 수 있다.

3. 전문가 설문조사: 또 다른 방법은 경제 전문가들을 대상으로 설문조사를 실시하고 그 응답을 사용하여 정책 불확실성을 측정하는 것이다. 여기에는 정책금리 또는 기타 통화 정책 조치의 예상 미래 경로에 대한 질문을 포함할 수 있다. 전문가들의 응답 간의 분산 또는 불일치는 불확실성의 척도로 사용될 수 있다.

4. 계량경제학 모델: GARCH 모델과 같은 계량경제학 모델도 정책 불확실성을 측정하는 데 사용된다. 이러한 모델은 중앙은행 정책에 영향을 받을 수 있는 경제 변수의 변동성을 추정한다. 예를 들어, 인플레이션 또는 환율과 같은 것이다.

5. 기계학습: 기계학습 기술은 다양한 예측에 점점 더 많이 사용되고 있다. 예를 들어, 서포트 벡터 머신, 로지스틱 회귀 또는 신경망은 정책 불확실성과 관련된 문서를 분류하고 태그하는 데 사용될 수 있다.

나. 토픽 기반 방법의 장점

토픽 기반 방법은 경제 불확실성을 측정하는 데 있어 다른 방법에 비해 여러 가지 강점을 가지고 있다.

1. 포괄성: 특정 키워드에 의존하는 방법과 달리, 토픽 기반 접근법은 기사의 모든 단어 조합을 분석하여 기사의 내용과 토픽에 대한 보다 전체적인 이해를 제공한다. 이는 불확실성이 논의되는 맥락에 대한 포괄적인 이해를 제공한다.

2. 유연성: 특정 미리 정의된 키워드에 의존하는 경우, 때로는 거짓 긍정(False Positive, 기사가 모든 키워드를 포함하지만 실제로 측정되는 특정 유형의 불확실성과 관련이 없을 수 있음) 또는 거짓 부정(False Negative, 기사가 특정 키워드를 사용하지 않고 불확실성의 주제를 논의할 수 있음)이 발생할 수 있다. 토픽 기반 방법은 이러한 문제를 해결할 수 있다.

3. 모호성 해소: 토픽 기반 방법은 불확실성의 여러 유형을 구별할 수 있으며, 보다 세밀한 분석을 가능하게 한다. 예를 들어, 기사에서 "경제 및 금융 위기", "통화 정책 제도", "기술 및 기업"과 관련된 불확실성을 구별할 수 있다.

그러나 토픽 기반 방법에도 몇 가지 단점이 있다. 토픽 상관관계를 기반으로 라벨을 할당하는 과정은 주관적일 수 있으며, 측정 모형은 뉴스 미디어에서 자주 논의되지 않는 형태의 불확실성을 포착하지 못할 수 있다. 토픽 기반 방법 또한, 다른 방법과 마찬가지로, 경제 불확실성을 분석하기 위한 어러 도구 중 하나일 뿐이며, 다른 방법과 함께 사용될 때 가장 효과적일 것으로 기대된다.

다. 토픽 모형

토픽 모델링은 문서 모음에서 주요 주제를 자동으로 식별하는 비지도 기계학습 기술이다. 이 방법은 텍스트의 숨겨진 토픽의 패턴을 발견하고 이러한 토픽을 기반으로 문서를 분류하는 방법을 제공한다.
토픽 모델링의 결과는 토픽 또는 주제를 구성하는 단어의 확률 분포이다. 이는 토픽을 설명하는 데 사용되는 단어의 가중치이다. 토픽 모델링의 결과는 또한 각 문서의 토픽 혼합을 나타내는 토픽 분포이다. 이는 문서가 각 토픽에 대해 얼마나 많은 단어를 사용하는지를 나타낸다. 아이디어는 동일한 토픽에 대한 문서에서 특정 단어 조합이 함께 나타나는 경향이 있다는 것이다. 예를 들어, 통화 정책에 관한 문서는 "이자", "금리", "중앙은행", "인플레이션"과 같은 단어를 자주 사용할 수 있다.
토픽 모델링에 사용되는 여러 알고리즘 가운데 가장 많이 사용되는 것은 잠재 디리클레 할당(LDA)이다.

(가) 잠재 디리클레 할당 (Latent Dirichlet Allocation, LDA)

LDA는 각 문서는 일정한 수의 토픽이 혼합되어 있으며 문서에 존재하는 각 단어가 문서의 여러 토픽 중 하나에 속한다고 가정하는 생성 확률 모형이다. LDA의 "잠재"는 단어가 토픽에 할당되는 것이 관찰되지 않고 추론되어야 한다는 사실을 나타낸다.
잠재 디리클레 할당(LDA)과 같은 생성 모형은 데이터가 만들어진 과정을 모방하려고 한다. LDA는 이러한 생성과정을 역공학(reverse engineering)적으로 추론하여 데이터를 생성한 모델의 매개변수를 추정한다. 이러한 생성 모델은 데이터의 숨겨진 구조를 추론하는 데 사용된다.
사람이 기사나 문서를 작성할 때에는 일반적으로 여러 주제를 염두에 두고 글을 작성한다. 예를 들어, 기자가 캄보디아의 통화 정책에 대한 기사를 작성한다면 인플레이션, 이자율, 캄보디아 중앙은행의 역할과 같은 주제를 논의하려고 할 것이다. 작가는 각 단어에 대해 무작위로 주제를 선택하지 않고 마음속에 주제 분포를 가지고 있으며, 그 주제와 관련된 단어가 기사에 나타날 가능성이 더 크다. 작성 과정에서 저자는 주제 분포를 기반으로 주제를 선택하고 해당 주제의 단어 분포를 기반으로 단어를 쓴다. 이 과정은 기사가 완성될 때까지 반복된다. 이것이 LDA가 모델링하려고 하는 생성 과정이다.
LDA는 관찰된 데이터(문서의 단어)에서 이 데이터를 생성했을 수 있는 숨겨진 매개변수(각 문서의 토픽 분포 각 토픽의 단어 분포)로 돌아가려고 한다. 다음과 같은 방식으로 문서가 생성된다고 가정함으로써 이를 수행한다

1. 각 문서에 대해 디리클레 분포에서 토픽 분포가 선택된다. 각 토픽은 단어에 대한 분포로 표현된다.
2. 문서의 각 단어에 대해 토픽 분포에서 토픽이 선택된다.
3. 선택된 토픽의 단어 분포에서 단어가 선택된다.

관찰된 문서에서 거꾸로 작업함으로써 LDA는 숨겨진 토픽 구조를 추론할 수 있으며, 문서의 토픽 분포와 각 토픽의 단어 분포를 추정할 수 있다.

(나) 토픽의 수 (K)

토픽 모델링을 위해 잠재 디리클레 할당(LDA)을 사용할 때, 중요한 결정 중 하나는 모델의 토픽 수(일반적으로 "K"로 표시)이다. 토픽 수의 선정은 모델이 식별할 토픽이 얼마나 세분화될지를 결정하기 때문에 결과에 큰 영향을 미친다.
토픽 수가 너무 낮게 설정되면 모델은 매우 포괄적이고 구체적이지 않은 토픽을 생성할 수 있으며, 반면, 토픽 수가 너무 높게 설정되면 모델은 소수의 문서만을 다루는 매우 구체적인 토픽을 생성하거나 개념적으로 하나인 토픽을 여러 토픽으로 분할할 수 있다.
하지만, 토픽 수를 사전에 "올바르게" 선택하는 확실한 방법은 존재하지 않는다. 많은 경우 토픽 수는 연구자의 해당 분야 지식을 바탕으로 생성된 토픽 결과의 품질을 평가하는 반복적인 시행착오를 바탕으로 결정된다. 이를 위해 perplexity와 토픽 일관성(coherence)과 같은 측정치를 사용하여 토픽 수를 비교할 수 있다.

(다) 토픽 일관성 (Topic Coherence)

토픽 일관성은 각 토픽의 단어 구성이 의미적으로 얼마나 일관되어 있는지를 측정한다. 이는 사람들이 얼마나 쉽게 토픽을 해석할 수 있는지를 나타낸다. 즉, 토픽이 사람들에게 얼마나 해석 가능하고 의미 있는지를 정량화하려는 것이다. 토픽 일관성 측정접에는 여러 방법이 있지만 일반적으로 같은 논리를 따른다: 단어가 자주 공존하거나 의미적으로 유사한 토픽은 높은 일관성을 가져야 하며, 단어가 드물게 공존하거나 의미적으로 다른 토픽은 낮은 일관성을 가져야 한다. 토픽 일관성의 일반적인 측정치로는 C-V, C-UCI, C-NPMI와 U-Mass 등이 있다. <그림 4-1>은 토픽 수에 따른 토픽 일관성을 보여준다.

<그림 4-1>
토픽 수에 따른 토픽 일관성 수치 비교

라. 토픽 모델링 결과물

LDA 모델의 두 가지 중요한 결과물은 토픽-단어 분포와 문서-토픽 분포이다. 이 두 가지 분포는 토픽 모델링을 통해 생성된 토픽의 특성을 이해하는 데 도움이 된다. 이 절에서는 이 두 가지 분포에 대해 자세히 설명한다.


(가) 토픽-단어 분포

토픽-단어 분포는 단어가 특정 토픽의 일부일 확률을 나타내는 행렬이다. 이 분포를 통해 각 토픽의 구성을 이해할 수 있다. 이 분포는 캄보디아의 통화 정책과 관련된 주요 토픽 식별에 도움이 된다. 예를 들어, 어떤 토픽은 "달러화", "리엘", "환율", "통화"와 같은 단어를 높은 확률로 포함할 수 있으며, 이는 환율 관리에 중점을 둔 토픽을 나타낼 수 있다. 또 다른 토픽은 "인플레이션", "가격 안정", "소비자 물가 지수"와 같은 단어를 포함할 수 있으며, 이는 가격 안정 문제에 중점을 둔 토픽을 의미할 수 있다.

(나) 문서-토픽 분포

문서-토픽 분포는 문서(뉴스 기사)가 특정 토픽에 속할 확률을 나타내는 행렬이다. 이 분포를 통해 각 뉴스 기사에서 논의되는 주제를 이해할 수 있다. 이 분포는 각 기사에서 다루는 주요 토픽에 대한 정보를 제공할 수 있으며, 연장선상에서 통화 정책의 어떠한 측면이 언제 주요한 관심사였는지에 대한 정보를 제공할 수 있다. 예를 들어, 특정 날짜 주변의 많은 기사가 인플레이션과 관련된 토픽에 높은 확률을 가지고 있다면, 그 시기에 인플레이션 문제가 특히 두드러졌을 수 있음을 나타낼 수 있다. 또한 이러한 토픽 확률의 시간적 추세는 시간이 지남에 따른 통화 정책 불확실성의 변화에 대한 정보를 제공할 수 있다. 경제 불안정 기간이나 주요 정책 변경 기간 동안 특정 토픽에 대한 확률이 증가하면, 이는 해당 토픽이 통화 정책 불확실성의 주요 요인임을 나타낼 수 있다.

(3) LDA의 추정 및 불확실성 토픽의 식별

이 절에서는 불확실성과 관련된 토픽을 식별하고 정량화하는 방법론을 자세히 설명한다. 먼저 불확실성과 관련된 시드 단어 집합을 정의하여 특정 토픽-단어 분포를 초기화한 다음, EM (Expectation-Maximization) 알고리즘을 토픽-단어 분포와 문서-토픽 분포를 추정하기 위해 사용한다. E-단계에서는 관찰된 단어와 분포의 현재 추정치를 고려하여 토픽의 사후 분포를 계산한다:

그 후 M-단계에서는 이 사후 분포를 기반으로 토픽-단어 분포와 문서-토픽 분포의 추정치를 업데이트한다:

지시 함수 는 일 때 1이고 그렇지 않으면 0이다. 알고리즘이 수렴할 때까지 반복한 후, 시드 단어를 포함할 확률이 가장 높은 토픽을 불확실성과 관련된 토픽으로 식별한다. 
마지막으로 불확실성을 정량화하기 위해 각 문서에 대한 '불확실성 점수'를 계산한다. 이 점수는 문서 내의 불확실성과 관련된 토픽의 확률 합계로 계산된다. 따라서 더 높은 불확실성 점수를 가진 문서는 더 높은 수준의 정책 불확실성을 나타낸다. 이 방법은 정책 불확실성의 강도를 측정하기 위한 두 번째 LDA 모델의 기반이 된다.

라. 불확실성 정량화

다면적 정책 불확실성을 정량화를 위해, 본 연구는 두 개의 LDA 모델을 사용하는 이중 모델 접근법을 사용한다. 첫 번째 모델은 정책 불확실성의 토픽을 분류하고, 두 번째 모델은 불확실성의 강도를 측정한다. 이러한 이중 모델 접근법은 정책 불확실성에 대한 종합적인 이해를 제공한다. 이 접근법은 정책 불확실성의 전반적인 수준뿐만 아니라 불확실성이 다른 정책 영역에 어떻게 분배되는지도 포착한다. 이 접근법은 정책 불확실성의 구체적인 원인과 시간이 지남에 따라 어떻게 발전하는지에 대한 정보를 제공한다.

(가) 토픽 분류 모델 (모델 1)

첫 번째 LDA 모델은 환율 정책 불확실성, 통화 안정화 정책 불확실성, 디달러라이제이션 정책 불확실성, 해외 통화 정책 영향 불확실성과 같은 다양한 종류의 불확실성을 식별하는 데 목적이 있다. 이러한 토픽에 해당하는 시드 단어로 모델을 초기화하여, 이러한 토픽과 관련된 어휘를 학습하도록 모델을 유도한다. 토픽 수(K)는 비교적 크게 설정되었다. 이는 토픽이 불확실성의 다양한 유형을 포착할 수 있도록 하기 위함이다.

(나) 불확실성 강도 모델 (모델 2)

두 번째 LDA 모델은 기사 내의 불확실성 강도를 측정하는 데 목적이 있다. 이 모델은 불확실성과 관련된 미리 정의된 시드 단어 집합으로 초기화되어 토픽 모델링 과정을 유도한다. 각 문서의 '불확실성 점수'는 문서 내의 불확실성과 관련된 토픽의 확률 합계로 계산된다. 불확실성 점수가 높을 수록 불확실성이 더 높다는 것을 의미한다.

(3) 집계

마지막으로 집계 과정에서는 모델 2에서 얻은 불확실성 점수를 정책 불확실성의 시계열로 변환한다. 이 과정에는 시간 프레임을 결정하고, 점수를 정규화하고, 선택한 방법(평균, 중앙값 또는 합계)에 따라 집계하고, 최종 측정값을 해석하는 작업이 포함된다.
이중 모델 접근법을 통해 시간에 따른 각 토픽의 정책 불확실성 수준을 따라가는 정책 불확실성 지수를 생성할 수 있다. 예를 들어, 매월 환율 정책 불확실성 지수는 해당 범주에 분류된 모든 기사의 불확실성 점수를 평균화하여 계산될 수 있다. 다른 토픽에 대해 유사한 지수를 생성할 수 있다.
이러한 방법은 정책 불확실성의 구체적인 원인과 시간이 지남에 따라 어떻게 변화하는지에 대한 정보를 제공한다. 또한 이 방법은 정책 불확실성의 전반적인 수준뿐만 아니라 불확실성이 어떻게 구성되는지, 즉 불확실성이 다른 정책 영역에 어떻게 분배되는지도 파악할 수 있다.  기사에서 불확실성과 관련된 토픽의 상대적 비중은 불확실성의 강도를 나타내며, 결과를 다른 정책 불확실성 지표와 비교함으로써 이 가정을 검증할 수 있다.

1. 결과분석

이 절에서는 다단계의 불확실성 토픽모형 방법론의 적용 결과를 확인한다. 먼저 사전정보(Prior)를 사용하지 않는 토픽모형 결과를 제시하고, 그 다음 사전정보(Prior)를 적용한 토픽모형 결과를 제시한다. 마지막으로 2단계 불확실성 모형 결과를 제시한다.

가. 사전정보(Prior) 없는 토픽모형

사전정보(Prior)를 사용하지 않는 토픽모형은 39,637개의 캄보디아 뉴스 기사 데이터를 분석하여 내재되어 있는 토픽 구조를 발견하는 역할을 한다. 분석결과, 정치와 건강부터 기술과 국제 관계에 이르기까지 광범위한 주제를 대표하는 20개의 토픽이 식별되었다. <그림 5-1>의 워드클라우드는 이러한 다양한 토픽에 대한 시각적 표현이다. 예를 들어, 토픽 0은 선거와 거버넌스를 포함한 정치 역학에 중점을 둔 것으로 나타났으며, 토픽 1은 특히 COVID-19와 관련된 글로벌 보건 위기에 중점을 두었다. 토픽모형의 결과로 얻은 각 문서의 토픽분포는 문서를 분류하여 원하는 정보를 추출하는 데 사용된다.

<그림 5-1>
사전정보(Prior) 없는 토픽모형 결과 워드클라우드

나. 사전정보(Prior)를 적용한한 토픽모형

앞의 기본 토픽모형을 기반으로 하여, 사전정보(Prior)를 토픽모형에 적용한다. 이 방법은 중앙은행 정책과 관련된 토픽을 식별하는 데 목적이 있다. 앞선 모형의 결과 나타난 다양한 토픽 중에서 중앙은행 정책과 관련된 세분화된 토픽을 식별하기 위해 사전정보(Prior)를 사용한다. <그림 5-2>는 사전정보(Prior)를 적용한 토픽모형의 결과를 나타낸다.

<그림 5-2>
사전정보(Prior)를 적용한 토픽모형 결과 워드클라우드

다. 불확실성 토픽모형

불확실성 토픽모형 또한 2단계로 구성된다. 첫 번째 단계는 불확실성 사전정보(Prior)를 적용하여 불확실성과 관련된 토픽을 식별하는 것이고, 두 번째 단계는 불확실성의 다양한 측면을 포착하기 위해 세분화된 불확실성 사전정보(Prior)를 적용하여 불확실성 토픽을 세분화하는 것이다. <그림 5-3>은 1단계 불확실성 토픽모형의 결과를 나타낸다.

<그림 5-3>
1단계 불확실성 사전정보 기반 토픽모형 결과 워드클라우드

라. 중앙은행 정책 불확실성 정량화

본 연구의 최종 목표는 두 번째 단계의 불확실성 토픽모형을 기반으로 중앙은행 정책 불확실성을 정량화하는 것이다. 2단계 모형은 불확실성 토픽을 5개의 토픽으로 세분화하여 불확실성의 다양한 측면을 포착한다. 예를 들어, 토픽 0은 불확실성의 초기 단계를 나타내어 위험의 초기 지표를 포착한다. 토픽 1은 불확실성 대응 조치와 관련된 부분을 나타내며, 토픽 2는 금리 인하 또는 인상과 같이 중앙은행의 정책과 직접 관련된 부분을 나타낸다.
이상의 세 가지 토픽은 중앙은행 정책 불확실성에 대한 포괄적인 시각을 제공하며, 불확실성의 초기 단계, 반응적 조치, 중앙은행의 특정 조치를 구분한다. 이러한 세분화된 토픽은 중앙은행 정책 불확실성을 정량화하고 분석하는 데 중요한 기반이 된다. <그림 5-4>는 2단계 불확실성 토픽모형의 결과를 보여준다.

<그림 5-4>
2단계 불확실성 사전정보 기반 토픽모형 결과 워드클라우드

E. 토픽 추세

토픽 분포의 시간적 변화는 또 다른 측면에서 중앙은행 정책 불확실성의 변화를 이해하는 데 도움이 된다. <그림 5-5>의 2014년부터 2023년까지의 기간 동안 토픽비중 변화를 살펴보면, 경제 토픽은 하락 추세를 나타냈으며, 이는 글로벌 경제 환경의 변화나 관심의 전환을 반영할 수 있다 경제 토픽 비중의 지속적 감소는 데이터셋 내에서 일반 경제 지표에 대한 강조도가 줄어들었음을 나타낼 수 있다. 반면 뱅킹 토픽은 상승 추세를 보였으며, 2020년에 두드러진 급증이 있었다. 이는 규제 변화, 기술 발전 또는 특정 경제 이벤트로 인해 은행 및 금융 서비스에 대한 관심이 증가하고 있음을 나타낼 수 있다. 아세안 토픽의 변동, 특히 2020년의 큰 증가는 아세안 공동체 내에서의 지역 발전, 협력 또는 도전과 관련된 반영일 수 있다.

<그림 5-5>
토픽 추세

<그림 5-6>
불확실성 토픽 변화

<그림 5-6>은 다양한 측면에서 불확실성 토픽 변화 추세를 보여주고 있다. <그림 5-7>은 경제 토픽의 가중치가 0.5보다 큰 경우를 대상으로 한정하여 불확실성 강도를 측정한 결과로 경제 불확실성의 시간적 변화를 보여준다.

<그림 5-7>
경제관련 불확실성 토픽 변화

불확실성 시계열 그래프는 다양한 경제 이벤트에 의해 발생한 불확실성의 변화를 반영한 결과이다. 불확실성 수치의 고점은 중요한 경제 이벤트, 정책 변화 또는 시장 변동과 일치할 수 있다. 경제 토픽 가중치가 높은 문서에 중점을 둔 것은 불확실성이 특정 경제 지표, 정책 또는 부문과 어떻게 연결되는지에 대한 자세한 정보를 제공한다. 또한, 시계열 분석을 통해 계절 패턴, 주기적 추세 또는 일회성 이벤트에 대한 반응을 검토할 수 있게 하여, 경제분석 모형의 다면적 분석을 가능하게 한다.
본 연구의 결과는 기존 연구를 보완할 뿐만 아니라 추가적인 연구를 위한 기반을 제공한다. 향후 연구는 외부 경제지표와의 상관관계, 감정분석 또는 예측 모형에 대한 추가적인 분석을 포함할 수 있다. 또한, 본 연구는 다른 국가의 중앙은행 정책 불확실성에 대한 분석에도 적용될 수 있다.


마. 평가 및 검증

토픽모형 결과의 평가는 내러티브 접근법과 다른 경제 정책 불확실성 지수와의 비교를 통해 수행된다. 내러티브 접근법은 모형에서 산출된 불확실정 지표의 가장 높은 점수와 관련된 기사를 탐색하는 것으로 이루어진다. 이 과정을 통해 불확실성의 주요 원인을 분별하고, 모형의 식별이 기사의 실제 내용과 일치하는지 여부를 확인하는 데 목적이 있다. 예를 들어, 불확실성이 환율 정책, 통화 안정화 정책 또는 탈달러화 정책과 관련이 있는지에 대해 알아보고, 불확실성의 구체적인 원인을 파악하고 검증하는 과정이라고 할 수 있다. 본 연구에서 제공하는 파이썬 라이브러리를 사용하여 이러한 내러티브 접근법을 수행할 수 있다.
내러티브 접근법을 보완하는 방법으로 이미 존재하는 경제 불확실성 지수와의 비교를 통해 모형의 결과를 검증할 수 있다. 이러한 비교는 벤치마크 역할을 하며, 토픽모형 기반 불확실성 측정법을 다른 방법론과 비교할 수 있도록 한다. 상관관계 분석을 통해 두 지표 간의 관계를 평가할 수 있다.

1. 결론

본 연구는 Latent Dirichlet Allocation (LDA) 모형을 활용한 이중(듀얼) 모형 접근법을 사용하여 정책 불확실성을 분류하고 측정하였다. 이중 모형 접근법은 정책 불확실성의 전반적인 수준뿐만 아니라 이 불확실성이 다양한 측면을 포착하고 어떻게 구성되는지, 즉 불확실성이 다른 정책 영역에 어떻게 분배되는지를 파악할 수 있게 하며, 정책 불확실성의 구체적인 원인과 시간이 지남에 따라 어떻게 변화하는지에 대한 정보를 제공한다. 환율 정책 불확실성, 통화 안정화 정책 불확실성, 탈달러화 정책 불확실성과 같은 핵심 영역에 중점을 둠으로써 본 연구는 캄보디아의 달러라이제이션 통화 환경에서 불확실성에 기여하는 요소들의 복잡한 상호 작용을 보여준다.
본 연구에서 사용한 텍스트 데이터 기반 토픽모형의 정교한 적용은 중앙은행 정책 수립과 집행에 도움을 제공할 것으로 기대된다. 또한, 본 연구의 결과는 캄보디아 국립은행(NBC)이 실무적으로 활용할 수 있도록 라이브러리화 되어 제공된다. 이 라이브러리는 캄보디아의 중앙은행 정책 불확실성을 분류하고 측정하는 데 사용될 수 있다.


참고문헌

[References in English]

Azqueta-gavaldon, Andrés. Developing news-based economic policy uncertainty index with unsupervised machine learning. Economics Letters, 158:47–50, 2017.
Baker, Scott R., Nicholas Bloom, and Steven J Davis. Measuring economic policy uncertainty. The quarterly journal of economics, 131(4):1593–1636, 2016.
Kaveh-yazdy, Fatemeh and Sajjad Zarifzadeh. Measuring economic policy uncertainty using an unsupervised word embedding-based method. arXiv preprint arXiv:2105.04631, 2021.
Larsen, Vegard H. Components of uncertainty. International Economic Review, 62(2):769–788, 2021.
Miranda-belmonte, Hairo U., Victor Muñiz-sánchez, and Francisco Corona. Word embeddings for topic modeling: an application to the estimation of the economic policy uncertainty index. Expert Systems with Applications, 211:118499, 2023.