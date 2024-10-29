from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, 'student_register/student_list.html', context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            user = Student.objects.get(pk=id)
            form = StudentForm(instance=user)
        return render(request, 'student_register/student_form.html', {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            user = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/school/list')


def student_delete(request, id):
    user = Student.objects.get(pk=id)
    user.delete()
    return redirect('/school/list')


# # 模拟项目数据
# def project_list_view(request):
#     # 合规管理-项目运行-数据展示
#
#     # 获取查询参数
#     construction_unit = request.GET.get('construction_unit')
#     operation_unit = request.GET.get('operation_unit')
#     project_name = request.GET.get('project_name')
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')
#     page = request.GET.get('page', 1)  # 当前页码，默认是第一页
#     per_page = request.GET.get('per_page', 10)  # 每页显示的条数，默认10条
#
#     # 构建查询条件
#     query = Q()
#     if construction_unit:
#         query &= Q(construction_unit__icontains=construction_unit)
#     if operation_unit:
#         query &= Q(operation_unit__icontains=operation_unit)
#     if project_name:
#         query &= Q(name__icontains=project_name)
#     if start_date:
#         query &= Q(start_date__gte=start_date)
#     if end_date:
#         query &= Q(end_date__lte=end_date)
#
#     # 根据条件过滤数据
#     projects = Project.objects.filter(query).order_by('start_date')
#
#     # 分页处理
#     paginator = Paginator(projects, per_page)  # 分页器
#     try:
#         page_obj = paginator.page(page)
#     except EmptyPage:
#         # 如果请求页码超出范围，返回最后一页数据
#         page_obj = paginator.page(paginator.num_pages)
#
#     # 构建返回结果
#     project_list = [{
#         # 'id': project.id,
#         'project_name': project.project_name,
#         'construction_unit': project.construction_unit,
#         'operation_unit': project.operation_unit,
#         'Rating_infor': project.Rating_infor,
#         'status': project.status,
#         'start_date': project.start_date
#     } for project in page_obj]
#
#     response_data = {
#         'total_pages': paginator.num_pages,
#         'total_items': paginator.count,
#         'current_page': page_obj.number,
#         'per_page': per_page,
#         'projects': project_list
#     }
#
#     return JsonResponse(response_data)
#
#
# def project_files_view(request, project_id):
#     # 合规管理-项目运行-审核文件展示
#     try:
#         project = Project.objects.get(id=project_id)
#     except Project.DoesNotExist:
#         return JsonResponse({'error': 'Project not found'}, status=404)
#
#     # 获取项目的所有文件
#     files = project.files.all()
#     file_list = [{'file_name': file.file_name, 'file_url': file.file.url} for file in files]
#
#     return JsonResponse({'project': project.name, 'files': file_list})
#
#
# def download_file_view(request, file_id):
#     # 合规管理-项目运行-审核文件下载
#     try:
#         project_file = ProjectFile.objects.get(id=file_id)
#         file_handle = project_file.file.open()
#         response = FileResponse(file_handle)
#         response['Content-Disposition'] = 'attachment; filename="{}"'.format(project_file.file_name)
#         return response
#     except ProjectFile.DoesNotExist:
#         raise Http404("File not found")
#
#
# def approve_project_view(request, project_id):
#     # 合规管理-项目运行-通过审核
#     if request.method == 'POST':
#         # 在执行操作前需要二次确认，这部分在前端实现（通过弹窗等方式）
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             return JsonResponse({'error': 'Project not found'}, status=404)
#
#         # 更新审核状态为审核通过
#         project.audit_status = 'approved'
#         project.save()
#         return JsonResponse({'message': 'Project approved successfully'})
#     return JsonResponse({'error': 'Invalid request method'}, status=400)
#
#
# def reject_project_view(request, project_id):
#     # 合规管理-项目运行-拒绝审核
#     if request.method == 'POST':
#         reason = request.POST.get('rejection_reason', '')
#
#         # 验证拒绝原因字数
#         if len(reason) == 0 or len(reason) > 50:
#             return JsonResponse({'error': 'Rejection reason must be between 1 and 50 characters'}, status=400)
#
#         # 在执行操作前需要二次确认，这部分在前端实现（通过弹窗等方式）
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             return JsonResponse({'error': 'Project not found'}, status=404)
#
#         # 更新审核状态为审核拒绝，并保存拒绝原因
#         project.audit_status = 'rejected'
#         project.rejection_reason = reason
#         project.save()
#         return JsonResponse({'message': 'Project rejected successfully', 'rejection_reason': reason})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)