# viewport란?

ViewPort란 모바일 브라우저에서 웹컨텐트를 출력하는 영역으로써, 일반 PC의 브라우저에는 존재하지 않는 개념입니다. ViewPort는 웹페이지의 너비와 높이, 확대/축소 상태를 설정할 수 있게 해주며, 이를 통해 웹컨텐트가 최적의 상태로 표현될 수 있도록 도와줍니다.

- width: ViewPort의 가로크기를 지정합니다. 1024로 설정할 경우 ViewPort의 가로픽셀 개수는 1024개가 됩니다. 허용되는 값의 범위는 200~10,000입니다.
  height: ViewPort의 세로에 해당하는 픽셀의 개수입니다. 그 외 width와 동일한 특성을 가집니다.

- device-width, device-height: 각 모바일 장치마다 적절한 device-with, device-height 값이 설정되어 있습니다. 최근 대부분 모바일 장치에서는 device-width를 980px으로 설정하고 있습니다. width, height의 값으로 device-width, device-height를 지정할 수 있습니다.

- user-scalable: 사용자에게 줌인/줌아웃을 허용할지 여부를 설정합니다. 기본값은 yes입니다.

- initial-scale: 페이지가 최초로 로드될 때 사용할 기본 줌인/줌아웃 값입니다. 1은 100%를 의미하며, 0~10까지 허용합니다.

- minimum-scale: 최소 줌아웃 배율입니다. 지정한 배율 이하로 축소할 수 없게 할니다. 기본값은 0.25이며 0~10까지 값을 허용합니다.

- maximum-scale: 최대 줌인 배율입니다. 지정한 배율 이상으로 확대할 수 없게 합니다. 기본값은 1.6이며 0~10까지 값을 허용합니다.
