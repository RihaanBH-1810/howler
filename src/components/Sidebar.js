import CottageOutlinedIcon from '@mui/icons-material/CottageOutlined';
import ArticleIcon from '@mui/icons-material/Article';
import DownloadIcon from '@mui/icons-material/Download';
import SettingsIcon from '@mui/icons-material/Settings';
import { useNavigate } from 'react-router-dom';

function Sidebar() {
  const navigate = useNavigate();
  const handleHomeClick = () => {
    navigate('/');
  }
  const handleReportClick = () => {
    navigate('/report');
  }
  const handleDownloadClick = () => {
    navigate('/download');
  }
  const handleSettingClick = () => {
    navigate('/setting');
  }

  return (
    <aside id="sidebar">
        <div class="sidebar-title">
          <div class="sidebar-brand">
            <span class="material-icons-outlined"></span> PENETRATE
          </div>
        </div>
        <ul class="sidebar-list">
          <li class="sidebar-list-item" onClick={handleHomeClick}>
            <a target="_self">
              <span class="material-icons-outlined"><CottageOutlinedIcon/></span> Home
            </a>
          </li>
          <li class="sidebar-list-item" onClick={handleReportClick}>
            <a target="_self">
              <span class="material-icons-outlined"><ArticleIcon/></span> Report
            </a>
          </li>
          <li class="sidebar-list-item"  onClick={handleDownloadClick}>
            <a target="_self">
              <span class="material-icons-outlined"><DownloadIcon/></span> Download
            </a>
          </li>
          <li class="sidebar-list-item" onClick={handleSettingClick}>
            <a target="_self">
              <span class="material-icons-outlined"><SettingsIcon/></span> Settings
            </a>
          </li>
        </ul>
      </aside>
  );
}
export default Sidebar;