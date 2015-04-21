import sip
try:
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)
except ValueError, e:
    print e

import fancyqt.firefox_rc

values = {
    "ffWhite": "#fffdfc",
    "ffBackground": "#d6d2d0",
    "ffBackgroundAlternative": "#c7c3c0",
    "ffBorder": "#a09a94",
    "ffIconFill": "#797c80",
    "ffButtonHighlightMenu": "#edebea",
    "ffButtonHighlightMenuBorder": "#b2b0af",
    "ffButtonHighlightMain": "#f6f6f5",
    "ffButtonHighlightMainBorder": "#a0a0a0",
    "ffTooltip": "#443d39",
    "ffFontColorDark": "#221f1e",
    "ffHighlight": "#77B7E0",
    "ffHighlightLight": "#9BCAE9",
    "ffHighlightDark": "#055C94",
    "ffScrollbarBackground": "#afa7a3",
    "ffScrollbarHandleBorder": "#7d7875",
    "borderRadius": "3px",
}

style = """
QWidget </
    background: {ffWhite};
/>

QFrame </
    background: None;
    border: None;
/>

QMainWindow </
    background: None;
    border: None;
/>

QToolTip </
    background-color: {ffBackground};
    border: 1px solid {ffHighlight};
    color: {ffFontColorDark};
    padding: 3px;
    opacity: 200;
    border-radius: {borderRadius};
/>

QAbstractScrollArea </
    background: None;
    border: None;
/>

QTextEdit, QPlainTextEdit, QLineEdit, QAbstractSpinBox </
    background: {ffWhite};
    border: 1px solid {ffBorder};
    border-radius: {borderRadius};
    color: {ffFontColorDark};
    padding: 3px;
/>


QLabel </
    background: Transparent;
    border: None;
    padding: 3px;
/>

QAbstractSpinBox </
    min-width: 10ex;
/>

QAbstractSpinBox::up-button, QAbstractSpinBox::down-button
</
    background-color: None;
    subcontrol-origin: border;
    border: None;
/>

QAbstractSpinBox::up-button
</
    subcontrol-position: top right;
/>

QAbstractSpinBox::down-button
</
    subcontrol-position: bottom right;
/>

QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow </
    width: 10px;
    height: 10px;
/>

QAbstractSpinBox::up-arrow::hover, QAbstractSpinBox::down-arrow::hover </
    background-color: {ffButtonHighlightMainBorder};
/>

QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off </
    image: url(:/icons/black/arrow-up.svg);
/>

QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off </
    image: url(:/icons/black/arrow-down.svg);
/>


QAbstractButton, QAbstractButton::menu-button </
    background: None;
    border: None;
    border-radius: {borderRadius};
    padding: 3px;
    color: {ffFontColorDark};
/>


QAbstractButton </
    padding: 3px;
    min-width: 24px;
/>

QAbstractButton[popupMode="1"] </
    padding-right: 16px;        /* space for menu button */
/>

QAbstractButton::menu-button </
    background: None;
    width: 16px;
    margin: 1px;
    padding-right: 0px;
    subcontrol-origin: margin;
    subcontrol-position: right;
/>

QAbstractButton::hover </
    background: {ffButtonHighlightMenu};
    border: 1px solid {ffBorder};
/>

QAbstractButton::menu-button::hover</
    border: None;
    margin: 1px;
/>

QAbstractButton::checked, QAbstractButton::menu-button::checked </
    background: {ffButtonHighlightMenu};
    border: 1px solid {ffBorder};
/>

QAbstractButton::menu-button::checked </
    background: {ffButtonHighlightMenu};
    border: None;
/>

QAbstractButton::checked::hover, QAbstractButton::menu-button::checked::hover </
    background: {ffBackground};
    border: 1px solid {ffBorder};
/>

QAbstractButton::menu-button::checked::hover </
    background: {ffBackground};
    border: None;
/>



QComboBox, QAbstractItemView </
    background: {ffWhite};
    alternate-background-color: {ffButtonHighlightMenu};
    color: {ffFontColorDark};

    border-radius: {borderRadius};
    selection-background-color: {ffHighlight};
    selection-color: {ffWhite};
/>

QAbstractItemView::indicator </
    background: Transparent;
    border: 1px solid {ffBorder};
/>

QAbstractItemView::indicator::checked </
    image: url(:icons/black/kt-check-data.svg);
/>

QAbstractItemView::indicator::checked::selected </
    image: url(:icons/white/kt-check-data.svg);
/>

QCheckBox::indicator
</
    border: 1px solid {ffBorder};
    width: 10px;
    height: 10px;
/>

QCheckBox::indicator::checked </
    image: url(:icons/black/kt-check-data.svg);
/>

QRadioButton::indicator </
    border: 1px solid {ffBorder};
    border-radius: 5px;
/>

QRadioButton::indicator::checked </
    image: url(:icons/black/check-radio.svg);
    padding: 2px;
    width: 7px;
    height: 7px;
    border-radius: 6px;
/>



QTableView
</
    border-radius: {borderRadius};
    gridline-color: {ffBorder};
    background-color: {ffWhite};
/>

QHeaderView
</
    border: None;
    border-radius: 0px;
    background: {ffBackground};
/>

QHeaderView::section
</
    border-radius: 0px;
    background: {ffBackground};
    padding: 3px;
/>

QHeaderView::section::hover
</
    border-radius: 0px;
    background: {ffHighlight};
    color: {ffWhite};
/>

QHeaderView::section::horizontal
</
    border-left: None;
    border-right: None;
/>

QHeaderView::section::vertical
</
    border-top: None;
/>

QTableView QTableCornerButton::section </
     background: {ffBackground};
     border: None;
/>

QTableView::item, QListView::item, QTreeView::item </
    background: None;
    color: {ffFontColorDark};
    border: None;
    padding: 3px;
/>

QTableView::item::selected, QListView::item::selected, QTreeView::item::selected </
    background: {ffHighlight};
    color: {ffWhite};
    border: None;
/>

QTableView::item::pressed, QListView::item::pressed, QTreeView::item::pressed </
    background: {ffHighlight};
    color: {ffWhite};
    border: None;
/>




QComboBox </
    color: {ffFontColorDark};
    border: 1px solid {ffBorder};
    border-radius: {borderRadius};
    padding: 3px;
/>

QComboBox::drop-down
</
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    background: None;
    border-left: 0px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
/>

QComboBox::up-arrow, QComboBox::down-arrow
</
    width: 10px;
    height: 10px;
/>

QComboBox::up-arrow
</
    image: url(:/icons/black/arrow-up.svg);
/>

QComboBox::down-arrow
</
    image: url(:/icons/black/arrow-down.svg);
/>

QDateEdit::drop-down </
    background-color: Transparent;
    background-image: url(:/icons/black/arrow-down.svg);
    border: None;
    margin: 1px;
/>


QSlider::groove, QxtSpanSlider::groove </
    background: {ffBackground};
    border: 1px solid {ffBackgroundAlternative};
    border-radius: {borderRadius};
/>

QSlider::groove::horizontal </
    height: 6px;
    margin: 2px 0;
/>

QSlider::groove::vertical </
    width: 6px;
    margin: 0px 2px;
/>

QSlider::handle, QxtSpanSlider::handle </
    background: {ffBackgroundAlternative};
    border: 1px solid {ffScrollbarHandleBorder};
    border-radius: {borderRadius};
/>

QSlider::handle::horizontal </
    width: 16px;
    margin: -4px 0;
/>

QSlider::handle::vertical </
    height: 16px;
    margin: 0px -4px;
/>

QSlider::handle::hover, QxtSpanSlider::handle </
    background: {ffButtonHighlightMenu};
    border: 1px solid {ffBorder};
/>


QDial </
    background-color: {ffWhite};
    border: 1px solid {ffBorder};
/>

QDialog </
    background-color: {ffWhite};
    border: 1px solid {ffBorder};
/>


QGroupBox </
    border: None;
    border-radius: 0px;
    border-top: 1px solid {ffButtonHighlightMainBorder};
    margin-top: 1.6ex;
    padding-left: -3px;
    padding-right: -3px;
/>

QGroupBox::title </
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0.25ex;
    border-radius: 0px;
    color: {ffFontColorDark};
/>



QMenuBar </
    background-color: {ffBackground};
    color: {ffFontColorDark};
/>

QMenuBar::item </
    background: Transparent;
/>

QMenuBar::item:selected
</
    background: {ffHighlight};
    border: None;
/>

QMenuBar::item::pressed </
    border: None;
    background-color: {ffHighlight};
    color: {ffWhite};
    margin-bottom:-1px;
    padding-bottom:1px;
/>


QMenu </
    background: {ffBackground};
    border: 1px solid {ffBorder};
    border-radius: {borderRadius};
    margin: 2px;
/>

QMenu::icon </
    margin: 5px;
/>

QMenu::item </
    padding: 5px 30px 5px 30px;
    margin-left: 5px;
    border: 1px solid Transparent; /* reserve space for selection border */
/>

QMenu::item::selected </
    background: {ffHighlight};
    color: {ffWhite};
    margin: 3px;
    border-radius: {borderRadius};
/>

QMenu::item::checked </
    background: {ffButtonHighlightMenu};
    color: {ffFontColorDark};
    border: 1px solid {ffBorder};
    margin: 3px;
/>


QGraphicsView </
    border: 1px solid {ffBorder};
/>

DiagramWidget FigureCanvasQTAgg </      /* matplot */
    border: 1px solid {ffBorder};
/>



QProgressBar </
    border: 1px solid {ffBorder};
    border-radius: {borderRadius};
    text-align: center;
    padding: 1px;
    background: {ffWhite};
    color: {ffFontColorDark};
/>

QProgressBar[value="1"] </
    background: {ffWhite};
    color: {ffWhite};
/>

QProgressBar::chunk </
    background-color: {ffHighlight};
    border-radius: {borderRadius};
/>

QTabWidget </
    border: None;
/>

QTabWidget::pane </
    border-left: None;
/>

QTabBar
</
    qproperty-drawBase: 0;
    padding-right: 15px;
/>

QTabBar::tab </
    color: {ffFontColorDark};
    border: None;
    background: {ffBackground};
    background-color: None;
    padding-left: 5px;
    padding-right: 5px;
    padding-top: 2px;
    padding-bottom: 2px;
    margin-right: 0px;
/>

QTabBar::tab::top </
    border-bottom: None;
    background-color: None;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
/>

QTabBar::tab::bottom </
    border-top: None;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
/>

QTabBar::tab::top::selected </
    border-top: 3px solid {ffHighlight};
/>

QTabBar::tab::top::!selected </
    border-top: 3px solid {ffBorder};
/>

QTabBar::tab::bottom::selected </
    border-bottom: 3px solid {ffHighlight};
/>

QTabBar::tab::bottom::!selected </
    background-color: {ffBackground};
    border-left: 1px solid {ffBorder};
    border-right: 1px solid {ffBorder};
    border-bottom: 3px solid {ffBorder};
/>

QTabBar::tab::bottom::hover </
    border-bottom: 3px solid {ffHighlight};
/>

QTabBar::tab::top::hover </
    border-top: 3px solid {ffHighlight};
/>


QDockWidget </
    border: None;
    background: Transparent;
/>


QScrollBar </
    border: None;
    border-radius: 0px;
    background-color: {ffBackground};
/>

QScrollBar:horizontal </
    height: 12px;
    margin: 0px 12px 0px 12px;
/>

QScrollBar:vertical </
    width: 12px;
    margin: 12px 0px 12px 0px;
/>

QScrollBar::handle
</
    background-color: {ffBackgroundAlternative};
    border: 1px solid {ffScrollbarHandleBorder};
    border-radius: {borderRadius};
/>

QScrollBar::handle:horizontal
</
    min-width: 10px;
/>

QScrollBar::handle:vertical
</
    min-height: 10px;
/>

QScrollBar::handle:hover
</
    background-color: {ffButtonHighlightMenu};
    border: 1px solid {ffBorder};
/>

QScrollBar::add-line, QScrollBar::sub-line
</
    width: 10px;
    height: 10px;
    subcontrol-origin: margin;
    background-color: {ffBackground};
    border: 2px solid {ffScrollbarBackground};
    border-radius: {borderRadius};
/>

QScrollBar::add-line:hover, QScrollBar::sub-line:hover
</
    background-color: {ffBorder};
/>

QScrollBar::add-line:horizontal
</
    border-image: url(:/icons/black/arrow-right.svg);
    subcontrol-position: right;
/>

QScrollBar::sub-line:horizontal
</
    border-image: url(:/icons/black/arrow-left.svg);
    subcontrol-position: left;
/>

QScrollBar::add-line:vertical
</
    border-image: url(:/icons/black/arrow-down.svg);
    subcontrol-position: bottom;
/>

QScrollBar::sub-line:vertical
</
    border-image: url(:/icons/black/arrow-up.svg);
    subcontrol-position: top;
/>

QScrollBar::up-arrow, QScrollBar::down-arrow, QScrollBar::add-page, QScrollBar::sub-page
</
    background: None;
/>

QSplitter </
    background: {ffButtonHighlightMain};QProgressBar </
    border: 1px solid {ffBorder};
    border-radius: {borderRadius};
    text-align: center;
    padding: 1px;
    background: {ffWhite};
    color: {ffFontColorDark};
/>

QProgressBar[value="1"] </
    background: {ffWhite};
    color: {ffWhite};
/>

QProgressBar::chunk </
    background-color: {ffHighlight};
    border-radius: {borderRadius};
/>
/>

QSplitter::handle </
    margin: 1px;
/>

QSplitter::handle:horizontal </
    image: url(:icons/black/splitter-horizontal.svg);
    width: 2px;
/>

QSplitter::handle:vertical </
    image: url(:icons/black/splitter-vertical.svg);
    height: 2px;
/>

QSplitter::handle:pressed </
    /*image: url(images/splitter_pressed.png);*/
/>

QMainWindow::separator </
    background: {ffButtonHighlightMain};
    width: 6px;
    height: 6px;
    margin: 1px;
/>

QMainWindow::separator::vertical </
    image: url(:icons/black/splitter-horizontal.svg);
/>

QMainWindow::separator::horizontal </
    image: url(:icons/black/splitter-vertical.svg);
/>



QgsSpafMapCanvas </
    border: None;
/>

QgsSpafMapCanvas QFrame </
    background: {ffWhite};
    border-radius: {borderRadius};
    color: {ffFontColorDark};
    border: 1px solid {ffBorder};
/>

QgsSpafMapCanvas QLabel </
    background: Transparent;
    border: None;
/>

QgsSpafMapCanvas QScrollArea QWidget </
    border-radius: {borderRadius};
/>


QgsSpafMapCanvas QProgressBar#progressBarTotal </
    border: None;
    border-radius: 0;
    text-align: center;
    padding: 0px;
    background: Transparent;
    color: {ffFontColorDark};
/>

QgsSpafMapCanvas QProgressBar#progressBarTotal::chunk </
    background-color: {ffHighlightLight};
    border-radius: 0;
/>

""".format(**values).replace("</", "{").replace("/>", "}")
# use xml like tags, {} are used by python.format